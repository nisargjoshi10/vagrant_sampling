import os
import sys
sys.path.append(os.getcwd())
import argparse
import numpy as np
import pandas as pd
from tqdm import tqdm
from configs.datasets_config import get_dataset_info

import torch

from qmugs import utils as qmugs_utils
from qmugs.utils import prop_key, compute_mean_mad, preprocess_batch

from vagrant.model import Vagrant
from vagrant.conformers import smiles_to_coords
from vagrant.utils import calc_entropy, preprocess_batch_from_inputs, calc_coherence

def init_model(args, ckpt):
    model = Vagrant(args, predict_property=args.predict_property, ckpt_file=ckpt)
    model.args.sample_method = args.sample_method
    model.args.decode_method = args.decode_method
    model.args.temp = args.temp
    model.args.batch_size = args.batch_size
    model.args.mads = args.mads
    model.args.means = args.means
    model.args.device = args.device
    model.args.dtype = args.dtype
    return model

def gen(args):
    # Set up device and dtype
    args.cuda = torch.cuda.is_available()
    args.device = torch.device("cuda" if args.cuda else "cpu")
    args.dtype = torch.float32

    # Set up storage
    os.makedirs(args.sample_dir, exist_ok=True)
    gen_name = '{}_{}_{}'.format(args.name, args.sample_method, args.ckpt_epoch)
    os.makedirs(os.path.join(args.sample_dir, gen_name), exist_ok=True)
    gen_path = os.path.join(args.sample_dir, gen_name, '{}_gen.csv'.format(args.name))

    # Load data
    args.properties = [prop_key[prop] for prop in args.properties]
    if len(args.properties) > 0:
        args.predict_property = True
    else:
        args.predict_property = False
    dataset_info = get_dataset_info('qmugs', remove_h=args.remove_h)
    raw_train, raw_val, raw_test, raw_string, raw_props, args = qmugs_utils.load_datasets(args)
    args.means, args.mads = compute_mean_mad(raw_props)
    included_species = torch.Tensor(dataset_info['atomic_nb'])[None, :].int().view(-1,)
    bond_types = torch.tensor([1,2,3,4])

    # Load model
    ckpt = 'checkpoints/{}/{}_{}.ckpt'.format(args.name, args.ckpt_epoch, args.name)
    model = init_model(args, ckpt)
    args.charge_power = model.args.charge_power
    args.charge_scale = model.args.charge_scale
    print(model)

    # Calculate latent entropy
    try:
        train_mems = np.load('checkpoints/{}/train_mems.npy'.format(args.name))
    except FileNotFoundError:
        print('calculating train mems...')
        transform = qmugs_utils.QMugsTransform(dataset_info, args.device)
        dataset = qmugs_utils.QMugsDataset(raw_train, raw_string, raw_props, transform=transform)
        train_loader = qmugs_utils.QMugsDataLoader(dataset, batch_size=args.batch_size, shuffle=False)
        train_mems = np.empty((0,128))

        n_train_batches = 1000
        for i, data in enumerate(tqdm(train_loader, total=n_train_batches)):
            if i >= n_train_batches:
                break
            nodes, atom_positions, edges, edge_attr, atom_mask,\
            edge_mask, n_nodes, y_true, y0, y_mask, props, scaled_props = preprocess_batch(data, args)
            mu, _ = model.encode(nodes, atom_positions, edges, edge_attr, atom_mask, edge_mask, n_nodes)
            train_mems = np.concatenate([train_mems, mu.detach().cpu().numpy()])
        np.save('checkpoints/{}/train_mems.npy'.format(args.name), train_mems)
    train_entropy = calc_entropy(train_mems)
    high_entropy_dims = np.where(train_entropy >= 5.)[0]
    low_entropy_dims = np.where(train_entropy < 5.)[0]
    print('calculated latent entropy...')

    # Generate samples
    print('generating {} samples...'.format(args.n_samples))
    if args.sample_method == 'direct':
        gen, pred_props, sampled_z = model.sample_direct(args.n_samples)
    elif args.sample_method == 'robust':
        gen, pred_props, sampled_z = model.sample_robust(args.n_samples, args.n_perturbations, args.radius,
                                                         high_entropy_dims, low_entropy_dims)

    # Calculate incoherence
    if args.calc_coherence:
        # Reconstruct 3D molecular structures from SMILES
        pos, charge, one_hot, one_hot_edges, smiles, regen_idxs = smiles_to_coords(gen, included_species,
                                                                                   bond_types, dataset_info)

        # Pass reconstructed 3D molecules through encoder
        z_prime = torch.empty(0,128)
        for i in range(0, pos.shape[0], args.batch_size):
            batch_positions = pos[i:i+args.batch_size]
            batch_charges = charge[i:i+args.batch_size]
            batch_one_hot = one_hot[i:i+args.batch_size]
            batch_one_hot_edges = one_hot_edges[i:i+args.batch_size]
            nodes, atom_positions, edges, edge_attr,\
            atom_mask, edge_mask, n_nodes = preprocess_batch_from_inputs(batch_positions, batch_one_hot,
                                                                         batch_charges, batch_one_hot_edges,
                                                                         args)
            mu, _ = model.encode(nodes, atom_positions, edges, edge_attr, atom_mask, edge_mask, n_nodes)
            z_prime = torch.cat([z_prime, mu.detach().cpu()])

        # Reconstruct molecules from z_prime
        if args.sample_method == 'direct':
            regen, _, _ = model.sample_direct(z_prime.shape[0], from_z=True, z=z_prime)
        elif args.sample_method == 'robust':
            regen, _, _ = model.sample_robust(z_prime.shape[0], args.n_perturbations, args.radius,
                                              high_entropy_dims, low_entropy_dims, from_z=True,
                                              z=z_prime)
        incoherence = calc_coherence(gen, regen, regen_idxs, dist=True)

    else:
        incoherence = [None] * args.n_samples

    # Write data
    data = {'smiles': gen,
            'predicted_property': pred_props[:,0],
            'incoherence': incoherence}
    data = pd.DataFrame(data)
    data.to_csv(gen_path, index=False)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    ### I/O Parameters
    parser.add_argument('--name', required=True, type=str)
    parser.add_argument('--ckpt_epoch', default='1000', type=str)
    parser.add_argument('--sample_dir', default='samples', type=str)
    parser.add_argument('--distributed', default=False, action='store_true')

    ### Sample Parameters
    parser.add_argument('--n_samples', default=10000, type=int)
    parser.add_argument('--sample_method', choices=['direct', 'robust'],
                        default='direct', type=str)
    parser.add_argument('--decode_method', choices=['greedy', 'temp'],
                        default='greedy', type=str)
    parser.add_argument('--temp', default=0.5, type=float)
    parser.add_argument('--n_perturbations', default=100, type=int)
    parser.add_argument('--radius', default=0.1, type=float)

    ### Data Parameters
    parser.add_argument('--data_dir', default='./data/qmugs', type=str)
    parser.add_argument('--batch_size', default=100, type=int)
    parser.add_argument('--num_workers', default=0, type=int)
    parser.add_argument('--max_length', default=125, type=int)
    parser.add_argument('--remove_h', default=False, action='store_true')
    parser.add_argument('--max_heavy_atoms', default=50, type=int)
    parser.add_argument('--properties', nargs='+', default=[])
    parser.add_argument('--calc_coherence', default=False, action='store_true')
    args = parser.parse_args()
    gen(args)
