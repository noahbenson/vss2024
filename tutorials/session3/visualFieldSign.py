import sys
import os
import argparse
os.chdir('/cvmfs/neurodesk.ardc.edu.au/containers/deepretinotopy_1.0.2_20231223/deepretinotopy_1.0.2_20231223.simg/opt/deepRetinotopy_TheToolbox/')
sys.path.append('.')
from utils.fieldSign import field_sign

def generate_signMaps(path):
    path_sub = path + 'deepRetinotopy/'
    sub = path_sub.split('/')[-3]
    print(sub)
    for hemisphere in ['lh', 'rh']:
        field_sign(path_sub, hemisphere,
                sub + '.fs_predicted_polarAngle_' + hemisphere + '_curvatureFeat_average.func.gii',
                sub + '.fs_predicted_eccentricity_' + hemisphere + '_curvatureFeat_average.func.gii')

if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument('--path', type=str)
    args = args.parse_args()

    generate_signMaps(str(args.path))