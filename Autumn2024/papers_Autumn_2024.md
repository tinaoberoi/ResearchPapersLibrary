#This is a collection of daily papers and their summaries in Autumn 2024

## Research Papers

### Paper 1
- **Date**: 2024-09-23
- **Title**: [Quantum resources of quantum and classical variational methods](https://arxiv.org/pdf/2409.13008)
- **Authors**: Thomas Spriggs, Arash Ahmadi, Eliska Greplova
- **Keywords**: keyword1, keyword2
- **Abstract**: 
Variational techniques have long been at the heart of atomic, solid-state, and many-body physics.
They have recently extended to quantum and classical machine learning, providing a basis for representing quantum states via neural networks. These methods generally aim to minimize the energy of a given ansätz, though open questions remain about the expressivity of quantum and classical variational ansätze. The connection between variational techniques and quantum computing, through variational quantum algorithms, offers opportunities to explore the quantum complexity of classical methods. We demonstrate how the concept of non-stabilizerness, or magic, can create a bridge between quantum information and variational techniques and we show that energy accuracy is a necessary but not always sufficient condition for accuracy in non-stabilizerness. Through systematic benchmarking of neural network quantum states, matrix product states, and variational quantum methods, we show that while classical techniques are more accurate in non-stabilizerness, not accounting for the symmetries of the system can have a severe impact on this accuracy. Our findingsform a basis for a universal expressivity characterization of both quantum and classical variational methods.
- **Summary**: 
  After optimising the quantum state (using classical or quantum state) to find the ground state energy, questions arises how well is the quantum state itself represented by our approximate representation. While variational minimization brings the system to the point in Hilbert space with the required energy, it is far from certain that the optimized state will structurally reflect the global properties of the system. In particular, especially long range correlations are known to pose a challenge. In this work, we assess the expressivity of both quantum and classical variational methods from a quantum computational complexity point of view: we analyze the amount of quantum resources that the variational ansätz expresses when optimized in accordance with the classical energy variational principle. How are we measuring quantum resources?  how far a given state is from being efficiently and exactly simulated on a classical computer. The quantum operations that allow for efficient, exact classical simulation are elements of the Clifford group. All the other operations are referred to as non-Clifford. To quantify how ‘far’ a given operation is from the Clifford group, a measure called magic, or non-stabilizerness,was introduced. In this work we set-up the framework to reconcile classical simulatability notions of quantum resource theory with the formalism of classical variational techniques. We used non-stabilizerness, a quantity that measure how far is a given state from being classically simulatable in a sense of Gottesmann-Knill theorem, as a figure of merit for quality of classical variational approximation of a quantum state. Specifically, we assessed nonstablizerness expressivity for three qualitatively different types of variational ansätz: tensor networks, neural networks and variational quantum circuits. We found, that when comparing the best model (in terms of energy performance) for each method with exact diagonalization, on average, there is a general trend for better energy to correspond to better approximation in non-stabilizerness. This is an encouraging observation that suggests that the state reconstructed as a result of classical variational procedure has a complexity structure that represents the exact quantum solution reasonably well. 

- **Miscellaneous**: Notes or additional information about the paper, like citations, related research, or next steps.

---

### Paper 2
- **Date**: 2024-09-24
- **Title**: [Efficient computation of cumulant evolution and full counting statistics: application to
infinite temperature quantum spin chains](https://arxiv.org/pdf/2409.14442)
- **Authors**: Angelo Valli, Kormos
- **Keywords**: Quantum generating functions (QGF)
- **Abstract**: We propose a numerical method to efficiently compute quantum generating functions (QGF) for
a wide class of observables in one-dimensional quantum systems at high temperature. We obtain
high-accuracy estimates for the cumulants and reconstruct full counting statistics from the QGF.
We demonstrate its potential on spin S = 1/2 anisotropic Heisenberg chain, where we can reach
time scales hitherto inaccessible to state-of-the-art classical and quantum simulations. Our results
challenge the conjecture of the Kardar–Parisi–Zhang universality for isotropic integrable quantum
spin chains.
- **Summary**: 
- **Miscellaneous**: 

---

### Paper 3 
- **Date**: 2024-09-24
- **Title**: [Gate Optimization of NEQR Quantum Circuits via PPRM
Transformation]([link](https://arxiv.org/pdf/2409.14629))
- **Authors**: Shahab Iranmanesh
- **Keywords**: Quantum Image Representation (QIR), Quantum Image Processing (QIP) 
- **Abstract**: Quantum image representation (QIR) is a key challenge in quantum image processing (QIP)
due to the large number of pixels in images, which increases the need for quantum gates
and qubits. However, current quantum systems face limitations in run-time complexity and
available qubits. This work aims to compress the quantum circuits of the Novel Enhanced
Quantum Representation (NEQR) scheme by transforming their Exclusive-Or Sum-of-Products
(ESOP) expressions into Positive Polarity Reed-Muller (PPRM) equivalents without adding
ancillary qubits. Two cases of run-time complexity—exponential and linear— are considered
for NEQR circuits with m controlling qubits (m → ∞), depending on the decomposition
of multi-controlled NOT gates. Using nonlinear regression, the proposed transformation is
estimated to reduce the exponential complexity from O(2m) to O(1.5
m), with a compression
ratio approaching 100%. For linear complexity, the transformation is estimated to halve the
run-time, with a compression ratio approaching 52%. Tests on six 256 × 256 images show
average reductions of 105.5 times for exponential cases and 2.4 times for linear cases, with
average compression ratios of 99.05% and 58.91%, respectively
- **Summary**: To decrease the run-time complexities of QIR schemes, researchers have proposed various optimizations and compressions, referred to as quantum image compressions (QICs). QIC aims to
reduce the quantum resources required for QIR by compressing a digital image before constructing
its quantum circuit, lowering the number of quantum gates, and simplifying quantum gates. 
- **Miscellaneous**: Any additional information
---

### Paper 3
- **Date**: 2024-09-24
- **Title**: [Performance of Parity QAOA for the Signed Max-Cut Problem]([link](https://arxiv.org/pdf/2409.14786))
- **Authors**: Anita Weidinger,Glen Bigan Mbeng
- **Keywords**: QAOA, MaxCut, Parity QAOA
- **Abstract**: The practical implementation of quantum optimization algorithms on noisy intermediate-scale
quantum devices requires accounting for their limited connectivity. As such, the Parity architecture was introduced to overcome this limitation by encoding binary optimization problems onto
planar quantum chips. We investigate the performance of the Quantum Approximate Optimization
Algorithm on the Parity architecture (Parity QAOA) for solving instances of the signed Max-Cut
problem on complete and regular graphs. By comparing the algorithms at fixed circuit depth, we
demonstrate that Parity QAOA outperforms conventional QAOA implementations based on SWAP
networks. Our analysis utilizes Clifford circuits to estimate lower performance bounds for Parity
QAOA for problem sizes that would be otherwise inaccessible on classical computers. For single
layer circuits we additionally benchmark the recursive variant of the two algorithms, showing that
their performance is equal.
- **Summary**: In this work, we study Parity QAOA to quantify better its advantages and disadvantages over vanilla QAOA.
To do so, we compare the algorithm’s performances
and hardware requirement on the signed Max-Cut problem [37], which includes the SK spin-glass considered
in Ref. [36] as a special case. We use Clifford preoptimization to estimate the algorithm’s performance
and hardware requirement for solving large problem instances, with sizes that go beyond the ones considered in
previous studies [35, 36]. We find that when a suitable
objective function is considered, Parity QAOA consistently outperforms vanilla QAOA at fixed circuit depth.
Finally, we address the limited spread of correlation in
Parity QAOA’s planar geometry by introducing a Parity recursive QAOA (RQAOA). We show that similarly
to its vanilla counterpart, Parity RQAOA overcomes the
obstacles to state preparation introduced by the local geometry.

- **Miscellaneous**: Any additional information
---

### Paper 4
- **Date**: 2024-09-24
- **Title**: [Efficient Large-Scale Quantum Optimization via Counterdiabatic Ansatz](https://arxiv.org/pdf/2409.15055)
- **Authors**: Jie Liu1 and Xin Wang
- **Keywords**: QAOA, DC-QAOA
- **Abstract**: Quantum Approximate Optimization Algorithm (QAOA) is one of the fundamental variational quantum algorithms, while a version of QAOA that includes counterdiabatic driving, termed Digitized Counterdiabatic QAOA
(DC-QAOA), is generally considered to outperform QAOA for all system sizes when the circuit depth for the two
algorithms are held equal. Nevertheless, DC-QAOA introduces more CNOT gates per layer, so the overall circuit
complexity is a tradeoff between the number of CNOT gates per layer and the circuit depth, and must therefore be carefully assessed. In this paper, we conduct a comprehensive comparison of DC-QAOA and QAOA
on MaxCut problem with the total number of CNOT gates held equal, and we focus on one implementation
of counterdiabatic terms using nested commutators in DC-QAOA, termed as DC-QAOA(NC). We have found
that DC-QAOA(NC) reduces the overall circuit complexity as compared to QAOA only for sufficiently large
problems, and for MaxCut problem the number of qubits must exceed 16 for DC-QAOA(NC) to outperform
QAOA. We have further shown that this advantage can be understood from the effective dimensions introduced
by the counterdiabatic driving terms. Moreover, based on our finding that the optimal parameters generated by
DC-QAOA(NC) strongly concentrate in the parameter space, we haved devised an instance-sequential training
method for DC-QAOA(NC) circuits, which, compared to traditional methods, offers performance improvement
while using even fewer quantum resources. Our findings provide a more comprehensive understanding of the
advantages of DC-QAOA circuits and an efficient training method based on their generalizability.
- **Summary**: In this paper, we compare DC-QAOA and QAOA on the
MaxCut problem [26], where the number of layers is increased until both algorithms reach the predefined fidelity
to the ground state of optimization problems. We use the
number of CNOT gates as an indicator of efficiency since it
characterizes the difficulty of implementing such algorithms
on quantum computers. Using MaxCut on randomly generated unweighted graphs as benchmarks, we found that for
graphs with over 16 vertices, DC-QAOA can achieve better performance using fewer two-qubit gates, while QAOA
is better for smaller graphs. By closely examining the effective dimension of the two circuits, we find that adding
cd-terms in each layer provides more effective dimensions
than simply adding more layers to QAOA, and the cd-terms
can suppress non-diagonal transitions, thereby improving DCQAOA’s performance. Furthermore, the optimal parameters
obtained by training DC-QAOA display a strong concentration in the parameter space, demonstrating potential transfer ability and generalizability from optimization problems on a
smaller scale to those on a larger scale. Based on our findings,
we devised an Instance-Sequential Training (IST) method for
DC-QAOA, which enables comparable or superior outcomes
with substantially reduced quantum resources. As a result,
DC-QAOA emerges as a more viable option for extensive
quantum optimization tasks, in contrast to QAOA, which may
be more efficient for smaller-scale problems.
- **Miscellaneous**: Any additional information
---

### Paper I (Add more as needed)
- **Date**: YYYY-MM-DD
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information

