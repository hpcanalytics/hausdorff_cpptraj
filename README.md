# Manual Hausdorff calculation for cpptraj

`cpptraj` can compute 2D RMSD matrices between two trajectories P and
Q. The script `hausdorff_manual.py` reads the 2D RMSD matrix and
calculates the [Hausdorff
distance](https://en.wikipedia.org/wiki/Hausdorff_distance) between P
and Q.

The Hausdorff distance calculations is calculated in the simple brute
force manner from the distance matrix.


## Usage

```
hausdorff_simple.py rmsd2.dat
```

This will print the Hausdorff distance to stdout.


## File format

The file format should be the distances between frames in trajectories
P and Q:

      # comment
      1  d_11 d_12 d_13 ... d_1,Nq
      2  d_21 d_22 d_23 ... d_2,Nq
      .
      .
      Np d_Np,1 d_Np,2 d_Np,3 ... d_Np,Nq

