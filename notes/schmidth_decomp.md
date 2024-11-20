# Schmidth Decomposition

Tool to analyse bipartite systems. 

**Bipartite Quantum Systems**
<hr>

A bipartite system is a composite system consisting of two subsystems A and B. Total Hibert space S of system H

$H = H_A \otimes H_B$

and the pure state $\psi$ in this composite system can be written as 

$|\psi> = \sum_{i, j}c_{ij}|u_i>_{A} \otimes |v_j>_{B}$

where, $|u_i>_{A}$ is the basis of $H_A$

where, $|v_j>_{B}$ is the basis of $H_B$

and $c_{ij}$ are complex coeff

Schmidth decomposition simplifies the above expression by transforming it to a special form where the state is represented as sum of uncorrelated terms. 

$|\psi> = \sum_k \lambda_k |u_k>_A |v_k>_B$

where $|u_k>_A$ and $|v_k>_B$ are orthonormal sets for basis vectors $H_A$ and $H_B$, and $\lambda_k \geq 0$ are schmidth coeff. And num of non-zero schmidth coeff is schmidth rank.

**Steps to obtain schmidth decomposition**

# Schmidt Decomposition Examples

## 1. **Correlated State Example**

Consider the following bipartite state of two qubits \( A \) and \( B \):

$
|\psi_{\text{correlated}}\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$

### Step 1: Write in tensor product form
$
|\psi_{\text{correlated}}\rangle = \frac{1}{\sqrt{2}} (|0\rangle_A \otimes |0\rangle_B + |1\rangle_A \otimes |1\rangle_B)
$

### Step 2: Identify Schmidt decomposition

The state is already in its Schmidt form:
$
|\psi_{\text{correlated}}\rangle = \sum_k \lambda_k |u_k\rangle_A \otimes |v_k\rangle_B
$

Here:
- **Schmidt coefficients**: $\lambda_1 = \lambda_2 = \frac{1}{\sqrt{2}}$.
- **Basis vectors**:
  
$|u_1\rangle_A = |0\rangle$ and $|v_1\rangle_B = |0\rangle$

$|u_2\rangle_A = |1\rangle$ and $|v_2\rangle_B = |1\rangle$

The Schmidt decomposition is:
$
|\psi_{\text{correlated}}\rangle = \frac{1}{\sqrt{2}} |0\rangle_A \otimes |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_A \otimes |1\rangle_B
$

---

## 2. **Uncorrelated State Example**

Now consider an **uncorrelated** bipartite state:
$
|\psi_{\text{uncorrelated}}\rangle = |0\rangle_A \otimes \left( \frac{1}{\sqrt{2}} |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_B \right)
$

### Step 1: Expand the state
$
|\psi_{\text{uncorrelated}}\rangle = \frac{1}{\sqrt{2}} |0\rangle_A \otimes |0\rangle_B + \frac{1}{\sqrt{2}} |0\rangle_A \otimes |1\rangle_B
$

### Step 2: Group terms
Factor out the common basis vector \( |0\rangle_A \):
$
|\psi_{\text{uncorrelated}}\rangle = |0\rangle_A \otimes \left( \frac{1}{\sqrt{2}} |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_B \right)
$

This is already in Schmidt form:
$
|\psi_{\text{uncorrelated}}\rangle = 1 \cdot |0\rangle_A \otimes \left( \frac{1}{\sqrt{2}} |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_B \right)
$

### Interpretation:
- **Schmidt coefficient**: \( \lambda_1 = 1 \).
- Only one term, so the Schmidt rank is **1** (product state, no entanglement).

---

## Summary

1. **Correlated State Schmidt Decomposition**:
   $
   |\psi_{\text{correlated}}\rangle = \frac{1}{\sqrt{2}} |0\rangle_A \otimes |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_A \otimes |1\rangle_B
   $
   - **Schmidt rank**: 2 (entangled).

2. **Uncorrelated State Schmidt Decomposition**:
   $
   |\psi_{\text{uncorrelated}}\rangle = |0\rangle_A \otimes \left( \frac{1}{\sqrt{2}} |0\rangle_B + \frac{1}{\sqrt{2}} |1\rangle_B \right)
   $
   - **Schmidt rank**: 1 (product state, no entanglement).


