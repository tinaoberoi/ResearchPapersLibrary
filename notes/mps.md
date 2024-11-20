# Matrix Product States

or tensor train is a framework where we factorise a tensor into multiple tensors. 

usually open systems easy to simulate in MPS, for periodic boundary conditions its more computationally expensive
https://arxiv.org/abs/1303.1333

```
typically use open boundary conditions, as they are more efficient within the MPS framework. However, I am also exploring ways to handle periodic boundary conditions, which can capture certain physical effects but are computationally more demanding in MPS.
```

Density Matrix Renormalization Group (DMRG) for ground state optimization because of its efficiency and accuracy in 1D systems. For time evolution, I utilize Time-Evolving Block Decimation (TEBD) or the Time-Dependent Variational Principle (TDVP), depending on the nature of the system.

main challenge: rapid growth of bond dimension

**MPS and entanglement entropy**

Now the bond dimension, quantifies how much entanglement the MPS can capture between two subsytems. Larger bond-dimension allows MPS to represent more entangled states. For a given quantum state, bond dimension will determine how well MPS can approximate it.

Entanglement Entropy in 1D systems $\rho_A = - Tr(\rho_A log \rho_A)$

and $\rho_A = Tr_B(|\psi\rangle \langle\psi|)$ reduced density matrix of A.

According to area law for 1D gapped systems, $S_A$ is constant, that is entanglement entropy of a subsytem A and rest of the system scales independently. thus limited enatanglement efficiently captured by MPS. 

Whereas in Gapless (critical systems), the entropy $S_A \propto L_A$ where $L_A$ is system size. Now larger bond dimension is required to efficiently simulate this system.

Given an MPS representation:
<hr>

You can compute the entanglement entropy between a subsystem and the rest by examining the singular values obtained from the Schmidt decomposition of the MPS across the bipartition.

Schmidt Decomposition in MPS

For a bipartition of the system at site \(k\):
$
|\psi\rangle = \sum_{\alpha} \lambda_{\alpha} |\phi_{\alpha}^A\rangle \otimes |\phi_{\alpha}^B\rangle
$

Where:

- $\lambda_{\alpha}$ are the Schmidt coefficients (related to singular values from the MPS).


The entanglement entropy is:
$
S_A = -\sum_{\alpha} \lambda_{\alpha}^2 \log \lambda_{\alpha}^2
$

The singular values $\lambda_{\alpha}$ are directly related to the bond dimensions of the MPS matrices. Therefore, the entanglement entropy $S_A$ provides insight into how large the bond dimension $\chi$ needs to be for an accurate MPS representation.

# DMRG

is an algorithm to optimise MPS. uch that after optimization, the MPS is approximately the dominant eigenvector of a large matrix H. 

# Summary of **DMRG Optimization in MPS**

The **Density Matrix Renormalization Group (DMRG)** is a variational algorithm designed to find the ground state of quantum systems efficiently. When combined with **Matrix Product States (MPS)**, it becomes a powerful tool for studying 1D quantum systems.

---

## **1. DMRG Framework**
- **Goal**: 
Minimize the energy $E = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}$ to find the ground state.
- **Wavefunction Representation**: Use an MPS to represent the quantum state:
$
  |\psi\rangle = \sum_{i_1, i_2, \dots, i_N} A^{[1]}_{i_1} A^{[2]}_{i_2} \cdots A^{[N]}_{i_N} |i_1 i_2 \dots i_N\rangle
$
  Each $A^{[k]}$ is a matrix (or tensor) associated with site \( k \).

---

## **2. Optimization Process**

DMRG optimizes the MPS tensors site by site (or pair of sites) through iterative **sweeps** across the lattice:

1. **Local Hamiltonian Construction**:
   - For site \( k \) (or sites \( k \) and \( k+1 \)), construct the **effective Hamiltonian** $H_{\text{eff}}$ by contracting all fixed tensors outside the target site(s).

2. **Solve Local Eigenvalue Problem**:
   - Solve the eigenvalue equation:
$
     H_{\text{eff}}^{[k, k+1]} \Psi = E \Psi
$
     Here:
     - $\Psi$: The **lowest-energy eigenvector**, which represents the optimal two-site wavefunction.
     - \( E \): The **lowest eigenvalue**, approximating the ground state energy contribution from these sites.

3. **Update MPS Tensors**:
   - Reshape $\Psi$ into a two-site tensor.
   - Perform **Singular Value Decomposition (SVD)**:
$
     \Psi \rightarrow U \Sigma V
$
     - Update $A^{[k]} \leftarrow U$ and $A^{[k+1]} \leftarrow \Sigma V$.
     - Truncate small singular values in $\Sigma$ to control the bond dimension $\chi$, ensuring computational efficiency.

1. **Canonical Form Maintenance**:
   - Ensure the MPS remains in **left- or right-canonical form** during the sweeps for numerical stability and efficient contraction.

---

## **3. Answer to Your Question**

### **"Do we just find the eigenvector \( \Psi \)?"**

Yes, the key computational step in DMRG is solving the local eigenvalue problem:
$
H_{\text{eff}}^{[k, k+1]} \Psi = E \Psi
$

- $\psi$  The lowest-energy eigenvector, which represents the **optimal two-site wavefunction**.
- Once $\psi$ is found, it’s reshaped and decomposed using **SVD** to update the MPS tensors for sites \( k \) and \( k+1 \).

The eigenvector \( \Psi \) is critical for optimizing the MPS representation of the ground state.

---

## **4. Why Two-Site Optimization?**

- **Flexibility**: Allows dynamic adjustment of bond dimension \( \chi \).
- **Improved Convergence**: More efficient than single-site optimization, particularly for systems with higher entanglement.

---

## **5. Key Advantages of DMRG**

- **Efficiency**: Works well for 1D and some 2D systems.
- **Accuracy**: Can provide near-exact ground state energies and observables for systems with low-to-moderate entanglement.
- **Scalability**: Adaptable to computational resources by adjusting bond dimension \( \chi \).

---

## **Conclusion**

DMRG iteratively optimizes MPS tensors by solving local eigenvalue problems and updating tensors through SVD. Solving for the eigenvector \( \Psi \) is a crucial part of refining the MPS to approximate the ground state of the system efficiently.


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
