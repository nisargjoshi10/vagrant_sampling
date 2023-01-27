qm9_with_h = {
    'name': 'qm9',
    'atom_encoder': {'H': 0, 'C': 1, 'N': 2, 'O': 3, 'F': 4},
    'atom_decoder': ['H', 'C', 'N', 'O', 'F'],
    'charge2idx': {1: 0, 6: 1, 7: 2, 8: 3, 9: 4},
    'n_nodes': {22: 3393, 17: 13025, 23: 4848, 21: 9970, 19: 13832, 20: 9482, 16: 10644, 13: 3060,
                15: 7796, 25: 1506, 18: 13364, 12: 1689, 11: 807, 24: 539, 14: 5136, 26: 48, 7: 16, 10: 362,
                8: 49, 9: 124, 27: 266, 4: 4, 29: 25, 6: 9, 5: 5, 3: 1},
    'max_n_nodes': 29,
    'atom_types': {1: 635559, 2: 101476, 0: 923537, 3: 140202, 4: 2323},
    'distances': [903054, 307308, 111994, 57474, 40384, 29170, 47152, 414344, 2202212, 573726,
                  1490786, 2970978, 756818, 969276, 489242, 1265402, 4587994, 3187130, 2454868, 2647422,
                  2098884,
                  2001974, 1625206, 1754172, 1620830, 1710042, 2133746, 1852492, 1415318, 1421064, 1223156,
                  1322256,
                  1380656, 1239244, 1084358, 981076, 896904, 762008, 659298, 604676, 523580, 437464, 413974,
                  352372,
                  291886, 271948, 231328, 188484, 160026, 136322, 117850, 103546, 87192, 76562, 61840,
                  49666, 43100,
                  33876, 26686, 22402, 18358, 15518, 13600, 12128, 9480, 7458, 5088, 4726, 3696, 3362, 3396,
                  2484,
                  1988, 1490, 984, 734, 600, 456, 482, 378, 362, 168, 124, 94, 88, 52, 44, 40, 18, 16, 8, 6,
                  2,
                  0, 0, 0, 0,
                  0,
                  0, 0],
    'colors_dic': ['#FFFFFF99', 'C7', 'C0', 'C3', 'C1'],
    'radius_dic': [0.46, 0.77, 0.77, 0.77, 0.77],
    'with_h': True}
    # 'bond1_radius': {'H': 31, 'C': 76, 'N': 71, 'O': 66, 'F': 57},
    # 'bond1_stdv': {'H': 5, 'C': 2, 'N': 2, 'O': 2, 'F': 3},
    # 'bond2_radius': {'H': -1000, 'C': 67, 'N': 60, 'O': 57, 'F': 59},
    # 'bond3_radius': {'H': -1000, 'C': 60, 'N': 54, 'O': 53, 'F': 53}}

qm9_without_h = {
    'name': 'qm9',
    'atom_encoder': {'C': 0, 'N': 1, 'O': 2, 'F': 3},
    'atom_decoder': ['C', 'N', 'O', 'F'],
    'charge2idx': {6: 0, 7: 1, 8: 2, 9: 3},
    'max_n_nodes': 29,
    'n_nodes': {9: 83366, 8: 13625, 7: 2404, 6: 475, 5: 91, 4: 25, 3: 7, 1: 2, 2: 5},
    'atom_types': {0: 635559, 2: 140202, 1: 101476, 3: 2323},
    'distances': [594, 1232, 3706, 4736, 5478, 9156, 8762, 13260, 45674, 174676, 469292,
                    1182942, 126722, 25768, 28532, 51696, 232014, 299916, 686590, 677506,
                    379264, 162794, 158732, 156404, 161742, 156486, 236176, 310918, 245558,
                    164688, 98830, 81786, 89318, 91104, 92788, 83772, 81572, 85032, 56296,
                    32930, 22640, 24124, 24010, 22120, 19730, 21968, 18176, 12576, 8224,
                    6772,
                    3906, 4416, 4306, 4110, 3700, 3592, 3134, 2268, 774, 674, 514, 594, 622,
                    672, 642, 472, 300, 170, 104, 48, 54, 78, 78, 56, 48, 36, 26, 4, 2, 4,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'colors_dic': ['C7', 'C0', 'C3', 'C1'],
    'radius_dic': [0.77, 0.77, 0.77, 0.77],
    'with_h': False}
    # 'bond1_radius': {'C': 76, 'N': 71, 'O': 66, 'F': 57},
    # 'bond1_stdv': {'C': 2, 'N': 2, 'O': 2, 'F': 3},
    # 'bond2_radius': {'C': 67, 'N': 60, 'O': 57, 'F': 59},
    # 'bond3_radius': {'C': 60, 'N': 54, 'O': 53, 'F': 53}}

geom_with_h = {
    'name': 'geom',
    'atom_encoder': {'H': 0, 'B': 1, 'C': 2, 'N': 3, 'O': 4, 'F': 5, 'Al': 6, 'Si': 7,
    'P': 8, 'S': 9, 'Cl': 10, 'As': 11, 'Br': 12, 'I': 13, 'Hg': 14, 'Bi': 15},
    'atomic_nb': [1,  5,  6,  7,  8,  9, 13, 14, 15, 16, 17, 33, 35, 53, 80, 83],
    'atom_decoder': ['H', 'B', 'C', 'N', 'O', 'F', 'Al', 'Si', 'P', 'S', 'Cl', 'As', 'Br', 'I', 'Hg', 'Bi'],
    'max_n_nodes': 181,
    'n_nodes': {3: 1, 4: 3, 5: 9, 6: 2, 7: 8, 8: 23, 9: 23, 10: 50, 11: 109, 12: 168, 13: 280, 14: 402, 15: 583, 16: 597,
                17: 949, 18: 1284, 19: 1862, 20: 2674, 21: 3599, 22: 6109, 23: 8693, 24: 13604, 25: 17419, 26: 25672,
                27: 31647, 28: 43809, 29: 56697, 30: 70400, 31: 82655, 32: 104100, 33: 122776, 34: 140834, 35: 164888,
                36: 185451, 37: 194541, 38: 218549, 39: 231232, 40: 243300, 41: 253349, 42: 268341, 43: 272081,
                44: 276917, 45: 276839, 46: 274747, 47: 272126, 48: 262709, 49: 250157, 50: 244781, 51: 228898,
                52: 215338, 53: 203728, 54: 191697, 55: 180518, 56: 163843, 57: 152055, 58: 136536, 59: 120393,
                60: 107292, 61: 94635, 62: 83179, 63: 68384, 64: 61517, 65: 48867, 66: 37685, 67: 32859, 68: 27367,
                69: 20981, 70: 18699, 71: 14791, 72: 11921, 73: 9933, 74: 9037, 75: 6538, 76: 6374, 77: 4036, 78: 4189,
                79: 3842, 80: 3277, 81: 2925, 82: 1843, 83: 2060, 84: 1394, 85: 1514, 86: 1357, 87: 1346, 88: 999,
                89: 300, 90: 390, 91: 510, 92: 510, 93: 240, 94: 721, 95: 360, 96: 360, 97: 390, 98: 330, 99: 540,
                100: 258, 101: 210, 102: 60, 103: 180, 104: 206, 105: 60, 106: 390, 107: 180, 108: 180, 109: 150,
                110: 120, 111: 360, 112: 120, 113: 210, 114: 60, 115: 30, 116: 210, 117: 270, 118: 450, 119: 240,
                120: 228, 121: 120, 122: 30, 123: 420, 124: 240, 125: 210, 126: 158, 127: 180, 128: 60, 129: 30,
                130: 120, 131: 30, 132: 120, 133: 60, 134: 240, 135: 169, 136: 240, 137: 30, 138: 270, 139: 180,
                140: 270, 141: 150, 142: 60, 143: 60, 144: 240, 145: 180, 146: 150, 147: 150, 148: 90, 149: 90,
                151: 30, 152: 60, 155: 90, 159: 30, 160: 60, 165: 30, 171: 30, 175: 30, 176: 60, 181: 30},
    'atom_types':{0: 143905848, 1: 290, 2: 129988623, 3: 20266722, 4: 21669359, 5: 1481844, 6: 1,
                  7: 250, 8: 36290, 9: 3999872, 10: 1224394, 11: 4, 12: 298702, 13: 5377, 14: 13, 15: 34},
    'colors_dic': ['#FFFFFF99',
                   'C2', 'C7', 'C0', 'C3', 'C1', 'C5',
                   'C6', 'C4', 'C8', 'C9', 'C10',
                   'C11', 'C12', 'C13', 'C14'],
    'radius_dic': [0.3, 0.6, 0.6, 0.6, 0.6,
                   0.6, 0.6, 0.6, 0.6, 0.6,
                   0.6, 0.6, 0.6, 0.6, 0.6,
                   0.6],
    'with_h': True}

geom_no_h = {
    'name': 'geom',
    'atom_encoder': {'B': 0, 'C': 1, 'N': 2, 'O': 3, 'F': 4, 'Al': 5, 'Si': 6, 'P': 7, 'S': 8, 'Cl': 9, 'As': 10,
                     'Br': 11, 'I': 12, 'Hg': 13, 'Bi': 14},
    'atomic_nb': [5,  6,  7,  8,  9, 13, 14, 15, 16, 17, 33, 35, 53, 80, 83],
    'atom_decoder': ['B', 'C', 'N', 'O', 'F', 'Al', 'Si', 'P', 'S', 'Cl', 'As', 'Br', 'I', 'Hg', 'Bi'],
    'max_n_nodes': 91,
    'n_nodes': {1: 3, 2: 5, 3: 8, 4: 89, 5: 166, 6: 370, 7: 613, 8: 1214, 9: 1680, 10: 3315, 11: 5115, 12: 9873,
                13: 15422, 14: 28088, 15: 50643, 16: 82299, 17: 124341, 18: 178417, 19: 240446, 20: 308209, 21: 372900,
                22: 429257, 23: 477423, 24: 508377, 25: 522385, 26: 522000, 27: 507882, 28: 476702, 29: 426308,
                30: 375819, 31: 310124, 32: 255179, 33: 204441, 34: 149383, 35: 109343, 36: 71701, 37: 44050,
                38: 31437, 39: 20242, 40: 14971, 41: 10078, 42: 8049, 43: 4476, 44: 3130, 45: 1736, 46: 2030,
                47: 1110, 48: 840, 49: 750, 50: 540, 51: 810, 52: 591, 53: 453, 54: 540, 55: 720, 56: 300, 57: 360,
                58: 714, 59: 390, 60: 519, 61: 210, 62: 449, 63: 210, 64: 289, 65: 589, 66: 227, 67: 180, 68: 330,
                69: 330, 70: 150, 71: 60, 72: 210, 73: 60, 74: 180, 75: 120, 76: 30, 77: 150, 78: 30, 79: 60, 82: 60,
                85: 60, 86: 6, 87: 60, 90: 60, 91: 30},
    'atom_types': {0: 290, 1: 129988623, 2: 20266722, 3: 21669359, 4: 1481844, 5: 1, 6: 250, 7: 36290, 8: 3999872,
                   9: 1224394, 10: 4, 11: 298702, 12: 5377, 13: 13, 14: 34},
    'colors_dic': ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14'],
    'radius_dic': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    'with_h': False}

def get_dataset_info(dataset_name, remove_h):
    if dataset_name == 'qm9':
        if not remove_h:
            return qm9_with_h
        else:
            return qm9_without_h
    elif dataset_name == 'geom':
        if not remove_h:
            return geom_with_h
        else:
            return geom_no_h
    else:
        raise Exception("Wrong dataset %s" % dataset_name)
