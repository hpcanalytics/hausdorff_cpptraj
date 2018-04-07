#!/usr/bin/env python
#
# Calculate the Hausdorff distance from cpptraj 2D RMSD data
#
# Copyright (c) 2018 Oliver Beckstein
# Released under the MIT License.

"""Calculate the Hausdorff distance from cpptraj 2D RMSD data. The
Hausdorff distance calculations is calculated in the simple brute
force manner from the distance matrix.

The file format should be the distances between frames in trajectories
P and Q:

      # comment
      1  d_11 d_12 d_13 ... d_1,Nq
      2  d_21 d_22 d_23 ... d_2,Nq
      .
      .
      Np d_Np,1 d_Np,2 d_Np,3 ... d_Np,Nq

The script just prints the Hausdorff distance to stdout.
"""

import numpy as np

def load_2drmsd(filename):
    d = np.loadtxt(filename)
    d = d[:, 1:]  # strip first column (frame number)
    return d

def Hausdorff_simple(d):
    hPQ = np.max(np.min(d, axis=1))
    hQP = np.max(np.min(d, axis=0))
    return np.max([hPQ, hQP])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("datafile", metavar="FILE",
                        help="cpptraj 2D RMSD file")


    args = parser.parse_args()

    d = load_2drmsd(args.datafile)
    dH = Hausdorff_simple(d)

    print(dH)

