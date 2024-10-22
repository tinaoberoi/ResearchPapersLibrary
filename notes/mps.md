# Matrix Product States

or tensor train is a framework where we factorise a tensor into multiple tensors. 

usually open systems easy to simulate in MPS, for periodic boundary conditions its more computationally expensive
https://arxiv.org/abs/1303.1333

```
typically use open boundary conditions, as they are more efficient within the MPS framework. However, I am also exploring ways to handle periodic boundary conditions, which can capture certain physical effects but are computationally more demanding in MPS.
```

Density Matrix Renormalization Group (DMRG) for ground state optimization because of its efficiency and accuracy in 1D systems. For time evolution, I utilize Time-Evolving Block Decimation (TEBD) or the Time-Dependent Variational Principle (TDVP), depending on the nature of the system.

main challenge: rapid growth of bond dimension
# DMRG

is an algorithm to optimise MPS. uch that after optimization, the MPS is approximately the dominant eigenvector of a large matrix H. 
