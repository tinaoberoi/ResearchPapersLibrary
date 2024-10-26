## SVD
https://builtin.com/articles/svd-algorithm

# Divide and conquer implementation SVD 
Implement on multi-node and multi-gpu version of this
[ref](https://scicomp.stackexchange.com/questions/1861/understanding-how-numpy-does-svd)


# Singular Value Decomposition (SVD) Algorithms

This guide covers four main algorithms used to compute the Singular Value Decomposition (SVD) of a matrix, focusing on their complexities, definitions, and usage scenarios.

## Algorithms and Complexities

| Algorithm                           | Complexity                      | Terms                                                                                              |
|-------------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------|
| Golub-Kahan Bidiagonalization + QR  | \( O(m^2 n) \)                 | - \( m \): Rows in \( A \) <br> - \( n \): Columns in \( A \)                                      |
| Divide-and-Conquer SVD              | \( O(n^3) \)                   | - \( n \): Size of square matrix \( A \)                                                          |
| Randomized SVD                      | \( O(mn \log k + k^2 m) \)     | - \( m \): Rows in \( A \) <br> - \( n \): Columns in \( A \) <br> - \( k \): Target rank          |
| Lanczos Algorithm                   | \( O(k \cdot \text{nnz}(A)) \) | - \( k \): Number of desired singular values <br> - \(\text{nnz}(A)\): Non-zero elements in \( A \) |

## Definitions

- **\( m \)**: Number of rows in matrix \( A \).
- **\( n \)**: Number of columns in matrix \( A \).
- **\( k \)**: Target rank or number of singular values desired.
- **\(\text{nnz}(A)\)**: Number of non-zero elements in matrix \( A \), important for sparse matrices.

## Python Example Code

Below is a Python example that computes the SVD of a matrix using NumPy and SciPy.

### Basic SVD Calculation with NumPy

```python
import numpy as np

# Create a random matrix A
A = np.random.rand(4, 3)

# Compute the SVD
U, s, VT = np.linalg.svd(A, full_matrices=False)

print("U Matrix:", U)
print("Singular Values:", s)
print("V^T Matrix:", VT)

```

## Diagonalisation of Matrix 
[source](https://www.statlect.com/matrix-algebra/matrix-diagonalization#:~:text=Matrix%20diagonalization%20is%20the%20process,Not%20all%20matrices%20are%20diagonalizable.)

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




### Singular Values and Eigenvalues

**Eigenvalue Definition**: Eigenvalues are defined for square matrices.

**Singular Values**: For non-square matrices, we use *singular values*. The singular values of an \( m \times n \) matrix \( A \) are the positive square roots of the nonzero eigenvalues of the corresponding matrix \( A^T A \).

**Singular Vectors**: The corresponding eigenvectors of \( A^T A \) are called *singular vectors*.


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

>
> If A's eigenvalues are distinct , then A doesnot hae defective eigenvalues. Therefore, possessing distinct eigenvalues is a sufficient condition for diagonalizability.\

<details>
<summary>How to diagonalise a matrix</summary>
<li>Compute eigenvalues of A</li>
<li>Check no eigenvalue is defective. If any eigenvalue is defective, then the matrix cannot be diagonalised. Else next step</li>
<li>If matrix is diagonalisable. For each eigenvalue find LI eigenvectors</li>
<li>Adjoin eigenvectors to form matrix P.</li>
<li>Build D.</li>
<li>The diagonalisation is done</li>
</details>

>The diagonalisation is not unqiue
> we can change the order in which the eogenvalues are put on D. Or we can replace a column of P with scalr multiple of itself. If there is a repreated eigenvaluem we can choose a different basis for its eigenspace.
