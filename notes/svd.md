## SVD
https://builtin.com/articles/svd-algorithm

> [!note] Solving QUBO with Gurobi > - **Presolve Phase**: Reduce complexity by removing redundant variables and constraints. > - **Bilinear Form**: For nonconvex QUBO problems, Gurobi reformulates them into a _bilinear form_ by introducing auxiliary variables. > - **Branch and Cut Method** > - **Termination**: Gurobi concludes the optimization process once all nodes have been explored or pruned.

## Diagonalisation of Matrix 

	Matrix diagonalisation is performing similarity transformation on a matrix in order to recover a similar matrix that is diagonal. Not all matrices are diagonalisable. Diagonalisable matrices are those that have no defective eigen values.

<details>
<summary>Similarity transformation</summary>
Two matrices A and B are said to be similar if there exists a matrix P such that

$B = P^{-1}AP$
If two matrices are similar they have same rank, trace, determinant and eigenvalues. 
</details>

<details> 
<summary>Diagonalisable Matrix</summary>
A is diagonalisable if and only if it is similar to diagonal matrix.
</details>

<details> 
<summary>Relationship to eigen values and eigenvectors</summary>
</details>




> [!note] Singular Values and Eigenvalues
> **Eigenvalue Definition**: Eigenvalues are defined for square matrices.
> 
> **Singular Values**: For non-square matrices, we use *singular values*. The singular values of an \( m \times n \) matrix \( A \) are the positive square roots of the nonzero eigenvalues of the corresponding matrix \( A^T A \).
> 
> **Singular Vectors**: The corresponding eigenvectors of \( A^T A \) are called *singular vectors*.

<details>
<summary>Example of singular value </summary>

calculation :

Consider the matrix A = [1 2; 3 4]. *Calculate A and A^T:.

A * A^T = [1 2; 3 4] * [1 3; 2 4] = [5 11; 11 25]

- **Find eigenvalues:**
    
    Solve the characteristic equation to find the eigenvalues of A * A^T which are approximately 0.29 and 29.71.
    
- **Take square roots:**
    
    The singular values of A are the square roots of the eigenvalues, which are approximately 0.54 and 5.45.
</details>

Relation to eigenvalues and eigenvectors:

$D = P^{-1}AP$
$AP = PD$

The kth column of AP is equal to $AP_{k}$, and kth column of PD is equal to $PD_{k}$
$D_{k}$ is the kth column of D, and the only non zero entry is $D_{kk}$
$PD_{k} = D_{kk}P_{k}$
$AP_{k} = D_{kk}P_{k}$

As a result $P_{k}$ is eigenvector and $D_{kk}$ is the eigen value. Thus the diagonal element of D are eigenvalues of A and columns of P are eigenvectors. The matrix P used in diagonalisation must be invertible. 

>[!note] 
> If A's eigenvalues are distinct , then A doesnot hae defective eigenvalues. Therefore, possessing distinct eigenvalues is a sufficient condition for diagonalizability.



Complexity of SVD

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


Friday:
- SVD (builtint)
- Diagonalisation
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