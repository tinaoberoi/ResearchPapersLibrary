# Cliffords

## Whats are clifford gates?

They map Pauli operator to another Pauli operator under conjugation.

A gate G is a Clifford gate if, for every Pauli operator P, applying G to P conjugates P into another Pauli operator. Mathematically: 

$$GPG^{†} ∈ {𝑋, Y, Z, I}$$ 

- H: maps X to Z
- S(Phase gate):Z to Z, X to Z
- CNOT Gate: 0 to 1

Together, the Hadamard, Phase, and CNOT gates form a universal set of Clifford gates.

Clifford Circuits: Circuits entirely made of clifford gates. 

## Why Clifford circuits?

1. Efficient Classical Simulation. 
One of the most interesting features of Clifford circuits is that they can be efficiently simulated on a classical computer using the Gottesman-Knill theorem. This is because the Clifford group (the set of all Clifford gates) does not generate computationally hard quantum operations by itself.

2. Role in Quantum Error Correction

## Drawbacks of cliffords

While Clifford gates are crucial in many areas of quantum computing, they do not form a universal gate set for quantum computation on their own. To achieve universal quantum computation (i.e., the ability to perform any possible quantum computation), non-Clifford gates like the T-gate are needed. Adding a T-gate to a Clifford circuit enables universal quantum computation.

