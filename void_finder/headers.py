#! python3.7

import argparse

#############################################################
#                                                           #
#                      DOCUMENTATION                        #
#                           and                             #
#                         PARSER                            #
#                                                           #
#############################################################

description = "This script generates a Random Catalog,\
 the Full Catalog and calls the Xiao-Dong Li's Fortran\
 Beta-Skeleton Calculator"
epilog = "At the end, the script stores a BetaSkeleton (.bsk) file."
parser = argparse.ArgumentParser(description=description, epilog=epilog)

parser.add_argument('input_name', type=str)
parser.add_argument('output_name', type=str)

parser.add_argument('-b', '--beta', type=float,
                    default=1.0,
                    help='Beta Skeleton Value, a float value "b>=1". Default Value = 1.0')
parser.add_argument('-n', '--nrand', type=float,
                    default=1.0,
                    help='The ratio between Number of Random Points and Number of Catalog Points (nrand= N_random/N_cat)')
parser.add_argument('-s', '--seed', type=int,
                    default=1,
                    help='The seed of the random number generator to create random catalogs.')
parser.add_argument('-A', '--ALGORITHM', type=str,
                    default="XDL",
                    help='Algorithm used to calculate .BSKIndex, Options: "NGL", "XDL"')
parser.add_argument('-T', '--TEST', 
                    action='store_true',
                    default=False,
                    help='Tests filenames and folders generating empty files, does not runs the hard calculations.')

arg = parser.parse_args()

BETA  = arg.beta
nrand = arg.nrand
SEED  = arg.seed
ALGORITHM   = arg.ALGORITHM
OC_FILE_IN  = arg.input_name
OUTPUT_NAME = arg.output_name
BSK_FILE_IN = arg.output_name


#############################################################
#                                                           #
#                   Paths and Filenames                     #                       
#                                                           #
#############################################################

OC_path = "./original_catalogs/"
RC_path = "./random_catalogs/"
FC_path = "./full_catalogs/"
BS_path = "./xdl_beta_skeleton/"
ML_path = "./masterlists/"
FG_PATH = "./figures/"
VE_PATH = "./volume_and_excentricity/"

OC_filename = "{}.cat".format(OC_FILE_IN)
RC_filename = "{}.cat".format(OUTPUT_NAME)
FC_filename = "{}.cat".format(OUTPUT_NAME)
BS_filename = "{}.BSKIndex".format(OUTPUT_NAME)
ML_filename = "{}.mls".format(OUTPUT_NAME)
VE_filename = "{}.vae".format(OUTPUT_NAME)

prog = "progress.txt"
