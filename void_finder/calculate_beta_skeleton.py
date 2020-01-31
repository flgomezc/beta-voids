#!/lustre/apps/anaconda/3.7/bin/python3
# Runing on the Magnus Cluster.
# Be sure to load the anaconda/python3.7 module.

import numpy as np
import os
import subprocess as subp
import timeit
import datetime

from headers import *
    
#############################################################
#############################################################
##                                                         ##
##                                                         ##
##                Begins the Main Routine                  ##
##                                                         ##
##                                                         ##
#############################################################
#############################################################
    
now = datetime.datetime.now()
toc = timeit.default_timer()

print("toc {}".format(toc))



N =  subp.getoutput("wc -l " + OC_path + OC_filename).split()
print("Original Catalog number of lines:", N[0])
try:
    OBS_CAT_SIZE = int( subp.getoutput("wc -l " + OC_path + OC_filename).split()[0] )
except:
    print("\n\t*** ERROR ***\n\n\t  \
--filein error: file '{}' not found. \
Are you sure that the 'filein' file is placed inside the \
'./original_catalogs/' folder? \n".format(OC_filename))

prog = "progress.txt"

progress_string = "echo  Init time: {} >> {}".format(now.isoformat(), prog)
subp.run( progress_string, shell=True, check=True)


#############################################################
#                                                           #
#                Generate RANDOM Catalogs                   #
#                                                           #
#############################################################    
### LOAD Original Catalog
print("Looking for: ", OC_path + OC_filename)
OC = np.loadtxt(OC_path + OC_filename)

N = OC.shape[0]

x_min = OC[:,0].min()
x_max = OC[:,0].max()
y_min = OC[:,1].min()
y_max = OC[:,1].max()
z_min = OC[:,2].min()
z_max = OC[:,2].max()

np.random.seed(SEED)  # This is a legacy function. Be aware!
Xrand = np.random.uniform(low=x_min, high=x_max, size=N)
Yrand = np.random.uniform(low=y_min, high=y_max, size=N)
Zrand = np.random.uniform(low=z_min, high=z_max, size=N)
RC = np.vstack([Xrand, Yrand, Zrand]).T

np.savetxt(RC_path + RC_filename, RC, delimiter=' ')
#############################################################
#                                                           #
#                 Generate FULL Catalogs                    #
#                                                           #
#############################################################    

### LOAD Random Catalog
#RC = np.loadtxt(RC_path + RC_filename)


### CREATE Full Catalog stacking RC and OC
FC = np.vstack([RC, OC])
 
now = datetime.datetime.now()
progress_string = "echo  Generating Full Catalog: {} at time {} >> {}".format(RC_filename, now.isoformat(), prog)
subp.run( progress_string, shell=True, check=True)
np.savetxt( FC_path + FC_filename, FC)


#############################################################
#                                                           #
#     Call BetaSkeletonCalc from Xiao-Dong Li's Lib         #
#                                                           #
#############################################################

subp.run("../beta-skeleton_finder/bin/LSS_BSK_calc -input  " + FC_path + FC_filename + 
         " -output " + str(BSK_FILE_IN) + 
         " -beta " + str(BETA) + 
         " -printinfo True -numNNB 300"
         , shell=True, check=True)

now = datetime.datetime.now()
progress_string = "echo  Generating {} Beta Skeleton: {} >> {}".format(BS_filename, now.isoformat(), prog)
subp.run( progress_string, shell=True, check=True)
tic = timeit.default_timer()

print("Time Elapsed: ", tic - toc)
