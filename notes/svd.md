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

**Complexity of svd**

```
 | d1
 A
|| d2
```
Assuming d2>d1, complexity of svd = O(d1d2^2)

https://en.wikipedia.org/wiki/QR_decomposition

**QR vs SVD**

SVD decomposition is a cannonical decomposition, which is numerically stable and avoids error propagation.

Consider solving the linear system:

$
A x = b
$

where:
$
A = \begin{bmatrix}
1 & 1 \\
1 & 1.0001
\end{bmatrix}, \quad
b = \begin{bmatrix}
2 \\
2.0001
\end{bmatrix}
$

The exact solution to this system is:
$
x = \begin{bmatrix}
1 \\
1
\end{bmatrix}
$

Now, introduce a small perturbation in \( b \):
$
b_{\text{perturbed}} = \begin{bmatrix}
2 \\
2.0002
\end{bmatrix}
$

We will solve this perturbed system using both QR decomposition and SVD and compare the results.

QR Decomposition
<hr>

Step 1: Perform QR Decomposition

The QR decomposition of \( A \) gives:
$
Q = \begin{bmatrix}
-0.7071 & -0.7071 \\
-0.7071 &  0.7071
\end{bmatrix}, \quad
R = \begin{bmatrix}
-1.4142 & -1.4143 \\
0 & -0.0000707
\end{bmatrix}
$

Step 2: Solve $QRx = b_{\text{perturbed}}$

First, solve $Q^T b_{\text{perturbed}}$:

$
Q^T b_{\text{perturbed}} = \begin{bmatrix}
-2.8283 \\
0.0000707
\end{bmatrix}
$

Next, solve $Rx = Q^T b_{\text{perturbed}}$:

$
\begin{bmatrix}
-1.4142 & -1.4143 \\
0 & -0.0000707
\end{bmatrix}
x = \begin{bmatrix}
-2.8283 \\
0.0000707
\end{bmatrix}
$

The solution is:
$
x_{\text{QR}} = \begin{bmatrix}
1.0000 \\
0.9999
\end{bmatrix}
$

Observation

- **Expected solution**: \( \begin{bmatrix} 1 \\ 1 \end{bmatrix} \)
- **Perturbed solution (QR)**: \( \begin{bmatrix} 1.0000 \\ 0.9999 \end{bmatrix} \)

The error in the solution is amplified due to the small value in \( R \), making QR decomposition less stable for ill-conditioned matrices.

2. Singular Value Decomposition (SVD)
<hr>

Step 1: Perform SVD

The SVD of \( A \) gives:

$
A = U \Sigma V^T
$
where:
$
U = \begin{bmatrix}
-0.7071 & -0.7071 \\
-0.7071 &  0.7071
\end{bmatrix}, \quad
\Sigma = \begin{bmatrix}
2.0001 & 0 \\
0 & 0.00005
\end{bmatrix}, \quad
V = \begin{bmatrix}
-0.7071 & -0.7071 \\
-0.7071 &  0.7071
\end{bmatrix}
$

Step 2: Solve \( Ax = b_{\text{perturbed}} \)

The solution using SVD is:
$
x_{\text{SVD}} = V \Sigma^+ U^T b_{\text{perturbed}}
$

Here, $( \Sigma^+)$ is the pseudoinverse of $\Sigma$:
$
\Sigma^+ = \begin{bmatrix}
\frac{1}{2.0001} & 0 \\
0 & \frac{1}{0.00005}
\end{bmatrix}
$

The solution is:
$
x_{\text{SVD}} = \begin{bmatrix}
1.00005 \\
0.99995
\end{bmatrix}
$

\subsection*{Observation}

- **Expected solution**: $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$
- **Perturbed solution (SVD)**: $\begin{bmatrix} 1.00005 \\ 0.99995 \end{bmatrix}$

The error in SVD is much smaller compared to QR decomposition due to the use of orthogonal matrices and explicit handling of singular values.

\section*{Summary of Error Propagation}

$
\begin{array}{|c|c|c|c|}
\hline
\text{Method} & \text{Expected Solution} & \text{Perturbed Solution} & \text{Error Amplification} \\
\hline
\text{QR Decomposition} & \begin{bmatrix} 1 \\ 1 \end{bmatrix} & \begin{bmatrix} 1.0000 \\ 0.9999 \end{bmatrix} & \text{Moderate} \\
\text{SVD} & \begin{bmatrix} 1 \\ 1 \end{bmatrix} & \begin{bmatrix} 1.00005 \\ 0.99995 \end{bmatrix} & \text{Minimal} \\
\hline
\end{array}
$

\section*{Conclusion}

- **QR decomposition** is moderately stable but can amplify errors for ill-conditioned matrices.
- **SVD** is highly stable due to its use of orthogonal matrices and explicit handling of singular values, making it more robust to perturbations.

The reason for minimal error in SVD is largely due to the \textbf{orthogonality} of the matrices involved, along with the explicit handling of singular values. Let's break this down:

1. Orthogonality of \(U\) and \(V\)

In the Singular Value Decomposition:
$
A = U \Sigma V^T
$
\(U\) and \(V\) are orthogonal matrices (or unitary if complex), meaning their columns are mutually orthogonal and normalized:
$
U^T U = I \quad \text{and} \quad V^T V = I
$

Why orthogonality helps:

- Preservation of vector norms: When you multiply a vector by an orthogonal matrix, it preserves its length (norm). This prevents the amplification of numerical errors.
- \Error damping: Any small perturbations in the data (e.g., errors introduced by rounding) are not magnified when multiplied by \(U\) or \(V\). Instead, the perturbations remain bounded.

For example:
$
\|Ux\| = \|x\| \quad \text{and} \quad \|Vy\| = \|y\|
$
This is not the case for non-orthogonal transformations, where errors can grow.

2. Singular Values in \(\Sigma\)

The diagonal matrix \(\Sigma\) contains the singular values \(\sigma_i\), which are non-negative and sorted:
$
\Sigma = \text{diag}(\sigma_1, \sigma_2, \dots, \sigma_r)
$

- Large singular values: Indicate directions in which the matrix stretches the data significantly.
- Small singular values: Indicate directions where the matrix compresses the data, which can cause instability if not handled properly.


In ill-conditioned systems, small singular values can make solving \(Ax = b\) numerically unstable. However, SVD isolates these small values in \(\Sigma\), making it clear which directions are problematic. This allows:

- Controlled handling of small singular values.
- Truncation or regularization to mitigate error amplification.


3. Comparison with Non-Orthogonal Methods

Other decompositions, like LU or QR, don’t leverage orthogonality as effectively:
- LU decomposition}, errors are amplified during row operations and pivoting because there’s no norm preservation.
- In \textbf{QR decomposition}, \(Q\) is orthogonal, which helps to some extent, but the upper triangular matrix \(R\) can still amplify errors, especially when dealing with small pivot elements (similar to LU).

4. Numerical Error in Back Substitution

When solving \(Ax = b\):
- In QR decomposition, the error propagates through solving \(Rx = Q^T b\). If \(R\) has small diagonal values, small perturbations in \(b\) can cause significant errors in \(x\).
- In SVD, solving involves:
  
$x = V \Sigma^+ U^T b$
    
Here, $\Sigma^+$ (pseudoinverse of $\Sigma$ dampens the effect of small singular values, and orthogonality of \(U\) and \(V\) ensures minimal propagation of errors.



