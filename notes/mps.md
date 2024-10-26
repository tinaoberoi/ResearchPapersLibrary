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

## MPS Calculations

https://www.tensors.net/p-tutorial-1

Given a density matrix calculate MPS
spectrum of density matrix
https://arxiv.org/pdf/2303.08738



Given a state vector generate MPS
Given an operator generate MPO code
get density matrix of circuit
TEBD

https://arxiv.org/pdf/1905.08768

Saturday:
- 6-8: Review (**complexity of SVD** and analyze computational requirements for different matrix sizes), revise yesterday's concepts
- 8-10: breakfast + MTE paper 2
- 10:00 - 1:00: tensor net tutorial 1
- 1:00 - 3:00 - Gym + Lunch
- 3:00 - 5:00 - Tensor net tutorial 2
- 9- 11 - Revise tutorial 1 and 2 + Classical solvers
Sunday:
- 6-8: tensornet tutorial 3
- 8-10: breakfast + hw1 and hw2
- 10 -