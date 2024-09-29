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

### Paper 5
- **Date**: 2024-09-28
- **Title**: [A Hybrid Quantum Neural Network for Split Learning](https://arxiv.org/abs/2409.16593)
- **Authors**: Hevish Cowlessur, Chandra Thapa
- **Keywords**: Hybrid Quantum Neural Network, Qubit-efficient data-loading technique,
Split Learning, Data Privacy Leakage, Reconstruction Attacks
- **Abstract**: Quantum Machine Learning (QML) is an emerging field of research with potential
applications to distributed collaborative learning, such as Split Learning (SL).
SL allows resource-constrained clients to collaboratively train ML models with a
server, reduce their computational overhead, and enable data privacy by avoiding raw data sharing. Although QML with SL has been studied, the problem
remains open in resource-constrained environments where clients lack quantum
computing capabilities. Additionally, data privacy leakage between client and
server in SL poses risks of reconstruction attacks on the server side. To address
these issues, we propose Hybrid Quantum Split Learning (HQSL), an application of Hybrid QML in SL. HQSL enables classical clients to train models with a
hybrid quantum server and curtails reconstruction attacks. In addition, we introduce a novel qubit-efficient data-loading technique for designing a quantum layer
in HQSL, minimizing both the number of qubits and circuit depth. Experiments
on five datasets demonstrate HQSL’s feasibility and ability to enhance classification performance compared to its classical models. Notably, HQSL achieves mean
improvements of over 3% in both accuracy and F1-score for the Fashion-MNIST
dataset, and over 1.5% in both metrics for the Speech Commands dataset. We
expand these studies to include up to 100 clients, confirming HQSL’s scalability.
Moreover, we introduce a noise-based defense mechanism to tackle reconstruction
attacks on the server side. Overall, HQSL enables classical clients to collaboratively train their models with a hybrid quantum server, leveraging quantum advantages while improving model performance and security against data privacy
leakage-related reconstruction attacks.
- **Summary**:We present a novel (to the best of our knowledge, the first) application of HQNN
to SL, which we call Hybrid Quantum Split Learning (HQSL), and study its security
concerning data privacy leakage. In a simple HQSL setup, the HQNN model is divided
into two parts: the client-side model, which has only classical neural network layers,
and the server-side model, which consists of a quantum layer followed by classical
neural network layers. The quantum layer consists of a quantum circuit that converts
classical inputs into quantum states, performs quantum computations, and outputs classical data. Considering the limitations of NISQ computers which restrict the number of qubits and circuit size, we employ a low-depth 2-qubit quantum circuit within the quantum layer. This also ensures our simulations have reasonable runtimes. To
allow a relatively larger dimension of classical data inputs into our quantum circuit,
we propose a qubit-efficient data-loading technique.

Quantum Circuit Design: We devise a qubit-efficient data-loading scheme, consisting of only 2 qubits and 3 layers of encoding and parameterized gates corresponding
to a 3-dimensional input. Through experimental analyses on the Fashion-MNIST
dataset (Xiao et al., 2017), we show that HQSL with our proposed circuit in
its quantum layer features a smaller simulation runtime and better classification
performance than deeper quantum circuits.

In HQNNs, classical and quantum
computing nodes are concatenated, with the classical layers reducing high dimensional
data to low dimensions to suit small quantum circuits that make up the quantum
layer (Schetakis et al., 2022; Alam et al., 2021). This approach is particularly important for current-generation quantum computers, which are constrained by quantum
circuit size and depth.
- **Miscellaneous**: Any additional information
---

### Paper 6
- **Date**: 2024-09-28
- **Title**: [Let the Quantum Creep In: Designing Quantum
Neural Network Models by Gradually Swapping
Out Classical Components]([link](https://arxiv.org/pdf/2409.17583))
- **Authors**: Peiyong Wang, Casey R. Myers
- **Keywords**: Quantum Machine Learning, Quanvolutional Neural Networks, Image
Classification
- **Abstract**: Artificial Intelligence (AI), with its multiplier effect and wide applications in multiple areas, could potentially be an important application of quantum computing.
Since modern AI systems are often built on neural networks, the design of quantum neural networks becomes a key challenge in integrating quantum computing
into AI. To provide a more fine-grained characterisation of the impact of quantum components on the performance of neural networks, we propose a framework
where classical neural network layers are gradually replaced by quantum layers
that have the same type of input and output while keeping the flow of information
between layers unchanged, different from most current research in quantum neural network, which favours an end-to-end quantum model. We start with a simple
three-layer classical neural network without any normalisation layers or activation
functions, and gradually change the classical layers to the corresponding quantum versions. We conduct numerical experiments on image classification datasets
such as the MNIST, FashionMNIST and CIFAR-10 datasets to demonstrate the
change of performance brought by the systematic introduction of quantum components. Through this framework, our research sheds new light on the design
of future quantum neural network models where it could be more favourable to search for methods and frameworks that harness the advantages from both the
classical and quantum worlds
- **Summary**: In this paper, we explore these issues by focussing on the transition from a fully
classical model to a classical-quantum hybrid model, HybridNet, in which the layers
are realised via (simulated) quantum circuits, but the information flow between layers
remains classical. As our main contribution, we propose such a gradual transition strategy for benchmarking the effectiveness of quantum neural network layers for particular
tasks. We proposed a novel trainable quanvolution [9] kernel, FlippedQuanv3x3, based
on the flipped model for quantum machine learning [10]. We also adopt the data
reuploading circuit [11], combined with the Hamiltonian embedding of classical data
[12, 13], as introduced in [14], DataReUploadingLinear, to mimic the effect of a
classical linear (dense) layer.

In general, the HybridModel with replacement level = 2 achieves the best average performance in all three datasets. The average performance of all three different
replacement levels degrades when the complexity of the data increases, from MNIST to
FashionMNIST and then to CIFAR-10. 

Compared to previous results from the quantum machine
learning literature on similar sets of data, such as in [14], our classical-quantum hybrid
neural network achieves a higher performance compared to an end-to-end quantum
neural network (96.9% versus 89.7% test accuracy on MNIST, and 86.6% versus 79.6%
on FashionMNIST).
- **Miscellaneous**: Any additional information
---

### Paper 7 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [Quantum DeepONet: Neural operators accelerated by quantum
computing](https://arxiv.org/pdf/2409.15683)
- **Authors**: Pengpeng Xiao1,2, Muqing Zheng
- **Keywords**: PDE, Neural Operators,
- **Abstract**: In the realm of computational science and engineering, constructing models that reflect realworld phenomena requires solving partial differential equations (PDEs) with different conditions.
Recent advancements in neural operators, such as deep operator network (DeepONet), which
learn mappings between infinite-dimensional function spaces, promise efficient computation of
PDE solutions for a new condition in a single forward pass. However, classical DeepONet entails quadratic complexity concerning input dimensions during evaluation. Given the progress
in quantum algorithms and hardware, here we propose to utilize quantum computing to accelerate DeepONet evaluations, yielding complexity that is linear in input dimensions. Our
proposed quantum DeepONet integrates unary encoding and orthogonal quantum layers. We
benchmark our quantum DeepONet using a variety of PDEs, including the antiderivative operator, advection equation, and Burgers’ equation. We demonstrate the method’s efficacy in both
ideal and noisy conditions. Furthermore, we show that our quantum DeepONet can also be
informed by physics, minimizing its reliance on extensive data collection. Quantum DeepONet
will be particularly advantageous in applications in outer loop problems which require to explore
parameter space and solving the corresponding PDEs, such as uncertainty quantification and
optimal experimental design
- **Summary**: While classical developments greatly expand the potential of neural networks, quantum neural networks (QNNs) have also drawn much attention due to the potential of better complexity
and higher capacities compared to their classical counterparts [28, 29, 30]. Such advantages often directly come from the ability to efficiently encode and explore the exponentially large space
on quantum computers [31]. Specifically, there are quantum algorithms that demonstrate the
quadratic speedup in online perceptron [32] and reinforcement learning [33], as well as the exponential speedup in linear-system solving [34, 35], least-square fitting [36], Boltzmann machine [37],
principal component analysis [38], and support vector machine. In this study, we design an architecture for quantum DeepONet and quantum physics-informed
DeepONet (QPI-DeepONet). To circumvent the trainability issue in QNN, we incorporate classical
training and quantum evaluation by employing the orthogonal neural network structure outlined
in Ref. [46]. Our work preserves the quadratic speed-up with respect to the input dimension
in the feed-forward pass from the quantum orthogonal neural network, with a minimal cost for
classical data preprocessing before training. The results of our numerical experiments suggest the
effectiveness of neural networks in solving different PDEs in both ideal and noisy environments.
Furthermore, we conducted a detailed analysis of the impact of quantum noise on our quantum
DeepONet, demonstrating how noise can influence performance and providing insights for the effect
of noise mitigation strategies. 
- **Miscellaneous**: Any additional information
---

### Paper 8
- **Date**: 2024-09-28
- **Title**: [An ensemble framework approach of hybrid Quantum convolutional neural networks for classification of breast cancer images](https://arxiv.org/abs/2409.15958)
- **Authors**: Dibyasree Guha
- **Keywords**: Parameterized Quantum Circuits · Hybrid Quantum Neural Network · Medical Image Classification
- **Abstract**: Quantum neural networks are deemed suitable to replace
classical neural networks in their ability to learn and scale up network
models using quantum-exclusive phenomena like superposition and entanglement. However, in the noisy intermediate scale quantum (NISQ)
era, the trainability and expressibility of quantum models are yet under investigation. Medical image classification on the other hand, pertains well to applications in deep learning, particularly, convolutional
neural networks. In this paper, we carry out a study of three hybrid
classical-quantum neural network architectures and combine them using standard ensembling techniques on a breast cancer histopathological
dataset. The best accuracy percentage obtained by an individual model
is 85.59. Whereas, on performing ensemble, we have obtained accuracy
as high as 86.72%, an improvement over the individual hybrid network
as well as classical neural network counterparts of the hybrid network
models.
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---

### Paper 9
- **Date**: 2024-09-28
- **Title**: [ULTRA-LOW LATENCY QUANTUM-INSPIRED MACHINE LEARNING
PREDICTORS IMPLEMENTED ON FPGA](https://arxiv.org/pdf/2409.16075)
- **Authors**: Lorenzo Borella
- **Keywords**: Tensor Networks · Machine Learning · Field Programmable Gate Arrays · High Energy Physics
- **Abstract**: Tensor Networks (TNs) are a computational paradigm used for representing quantum many-body
systems. Recent works have shown how TNs can also be applied to perform Machine Learning
(ML) tasks, yielding comparable results to standard supervised learning techniques.In this work, we
study the use of Tree Tensor Networks (TTNs) in high-frequency real-time applications by exploiting
the low-latency hardware of the Field-Programmable Gate Array (FPGA) technology. We present
different implementations of TTN classifiers, capable of performing inference on classical ML
datasets as well as on complex physics data. A preparatory analysis of bond dimensions and weight
quantization is realized in the training phase, together with entanglement entropy and correlation
measurements, that help setting the choice of the TTN architecture. The generated TTNs are then
deployed on a hardware accelerator; using an FPGA integrated into a server, the inference of the
TTN is completely offloaded. Eventually, a classifier for High Energy Physics (HEP) applications is
implemented and executed fully pipelined with sub-microsecond latency.
- **Summary**: In this work, several TTN architectures for binary classification are presented, solving common ML tasks as well
as harder classification problems coming from physics
datasets. Their quantum characteristics are explored to
investigate the distribution of the learned information, with
the aim of compressing said networks for optimized hardware deployment.
- **Miscellaneous**: Any additional information
---

### Paper 10
- **Date**: 2024-09-28
- **Title**: [Scalable quantum dynamics compilation via quantum machine learning](https://arxiv.org/pdf/2409.16346)
- **Authors**: Yuxuan Zhang 
- **Keywords**: Tensor netoworks, QML, cariational quantum compilation (VQC)
- **Abstract**: Quantum dynamics compilation is an important task for improving quantum simulation efficiency:
It aims to synthesize multi-qubit target dynamics into a circuit consisting of as few elementary
gates as possible. Compared to deterministic methods such as Trotterization, variational quantum
compilation (VQC) methods employ variational optimization to reduce gate costs while maintaining
high accuracy. In this work, we explore the potential of a VQC scheme by making use of out-ofdistribution generalization results in quantum machine learning (QML): By learning the action of
a given many-body dynamics on a small data set of product states, we can obtain a unitary circuit
that generalizes to highly entangled states such as the Haar random states. The efficiency in training
allows us to use tensor network methods to compress such time-evolved product states by exploiting
their low entanglement features. Our approach exceeds state-of-the-art compilation results in both
system size and accuracy in one dimension (1D). For the first time, we extend VQC to systems
on two-dimensional (2D) strips with a quasi-1D treatment, demonstrating a significant resource
advantage over standard Trotterization methods, highlighting the method’s promise for advancing
quantum simulation tasks on near-term quantum processors.
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---
### Paper 11
- **Date**: 2024-09-28
- **Title**: [Deep Circuit Compression for Quantum Dynamics via Tensor Networks](https://arxiv.org/pdf/2409.16361)
- **Authors**: Joe Gibbs and Lukasz Cincio
- **Keywords**: List of keywords
- **Abstract**: Dynamic quantum simulation is a leading application for achieving quantum advantage. However,
high circuit depths remain a limiting factor on near-term quantum hardware. We present a compilation algorithm based on Matrix Product Operators for generating compressed circuits enabling
real-time simulation on digital quantum computers, that for a given depth are more accurate than
all Trotterizations of the same depth. By the efficient use of environment tensors, the algorithm
is scalable in depth beyond prior work, and we present circuit compilations of up to 64 layers of
SU(4) gates. Surpassing only 1D circuits, our approach can flexibly target a particular quasi-2D
gate topology. We demonstrate this by compiling a 52-qubit 2D Transverse-Field Ising propagator
onto the IBM Heavy-Hex topology. For all circuit depths and widths tested, we produce circuits
with smaller errors than all equivalent depth Trotter unitaries, corresponding to reductions in error
by up to 4 orders of magnitude and circuit depth compressions with a factor of over 6.
- **Summary**: Simulating quantum dynamics is a leading application
for achieving a quantum advantage on near-term quantum computers, however the high circuit depths remain
prohibitive on current NISQ devices. To advance the
time to productive use of quantum computers, it is desirable to maximally use classical computation to optimize
quantum circuits so the algorithms are run more efficiently. In this direction, we build upon work performing
classical pre-computation and optimization of quantum
circuits, and present a compression of Trotter unitaries
for quantum dynamics. Our MPO-based optimization
found error reductions by up to a factor of 104
compared
to equivalent depth Trotterizations, or alternately for a
target error rate a depth compression up to a factor of
6.4. By the efficient use of environment tensors, our work
extends the literature by enabling far deeper circuit compilations than previously possible, optimizing our results
show the successful optimization of circuits with up to 64
layers of SU(4) gates. To demonstrate our approach can
flexibly compile to the connectivity of a target quantum
computer, we show the compression of a unitary directly
onto the 2D IBM Heavy-Hex topology.
- **Miscellaneous**: Any additional information
---
### Paper 12
- **Date**: 2024-09-28
- **Title**: [Non-stabilizerness Entanglement Entropy: a measure of hardness in the classical simulation of quantum many-body systems](https://arxiv.org/abs/2409.16895)
- **Authors**: Jiale Huang, Xiangjian Qian, Mingpu Qin
- **Keywords**: classical simulations, entanglement entropy
- **Abstract**: Classical and quantum states can be distinguished by entanglement entropy, which can be viewed
as a measure of quantum resources. Entanglement entropy also plays a pivotal role in understanding
computational complexity in simulating quantum systems. However, stabilizer states formed solely
by Clifford gates can be efficiently simulated with the tableau algorithm according to the GottesmanKnill theorem, although they can host large entanglement entropy. In this work, we introduce
the concept of non-stabilizerness entanglement entropy which is basically the minimum residual
entanglement entropy for a quantum state by excluding the contribution from Clifford circuits. It
can serve as a new practical and better measure of difficulty in the classical simulation of quantum
many-body systems. We discuss why it is a better criterion than previously proposed metrics such as
Stabilizer R´enyi Entropy. We also show numerical results of non-stabilizerness entanglement entropy
with concrete quantum many-body models. The concept of non-stabilizerness entanglement entropy
expands our understanding of the “hardness” in the classical simulation of quantum many-body
systems.
- **Summary**: Entanglement entropy is a well known metric, with the understanding that
higher entanglement entropy indicates greater difficulty
in classical simulation. Following the GottesmanKnill theorem [11, 12], it was recognized that the number of non-Clifford gate operations needed also serves as an indicator of simulation difficulty [35–40], since Clifford gate operations can be efficiently simulated on classical computers. This measure is also referred to as nonstabilizerness or quantum magic. Moreover, calculating the magic of a quantum system
is generally a hard problem [36, 37, 42–47]. Although numerous effective computational methods have been developed [43, 45, 48, 49], they are primarily applicable only
to small system sizes or special systems. In this work, we introduce a new metric termed Nonstabilizerness Entanglement Entropy (NsEE), which integrates entanglement entropy and quantum magic. We
show NsEE is a better metric to characterize the difficulty in the classical simulation of quantum many-body
systems
- **Miscellaneous**: Any additional information
---
### Paper 13
- **Date**: 2024-09-28
- **Title**: [Preparing Ground and Excited States Using Adiabatic CoVaR](https://arxiv.org/pdf/2409.16194)
- **Authors**: Wooseop Hwang, and B´alint Koczor
- **Keywords**: List of keywords
- **Abstract**: CoVarince Root finding with classical shadows (CoVaR) was recently introduced as a new
paradigm for training variational quantum circuits. Common approaches, such as variants of the
Variational Quantum Eigensolver, aim to optimise a non-linear classical cost function and thus suffer from, e.g., poor local minima, high shot requirements and barren plateaus. In contrast, CoVaR
fully exploits powerful classical shadows and finds joint roots of a very large number of covariances
using only a logarithmic number of shots and linearly scaling classical HPC compute resources. As
a result, CoVaR has been demonstrated to be particularly robust against local traps, however, its
main limitation has been that it requires a sufficiently good initial state. We address this limitation
by introducing an adiabatic morphing of the target Hamiltonian and demonstrate in a broad range
of application examples that CoVaR can successfully prepare eigenstates of the target Hamiltonian
when no initial warm start is known. CoVaR succeeds even when Hamiltonian energy gaps are very
small – this is in stark contrast to adiabatic evolution and phase estimation algorithms where circuit depths scale inversely with the Hamiltonian energy gaps. On the other hand, when the energy
gaps are relatively small then adiabatic CoVaR may converge to higher excited states as opposed
to a targeted specific low-lying state. Nevertheless, we exploit this feature of adiabatic CoVaR and
demonstrate that it can be used to map out the low lying spectrum of a Hamiltonian which can be
useful in practical applications, such as estimating thermal properties or in high-energy physics.
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---
### Paper 14
- **Date**: 2024-09-28
- **Title**: [QHyper: an integration library for hybrid
quantum-classical optimization](https://arxiv.org/pdf/2409.15926)
- **Authors**: Tomasz Lamza, Justyna Zawalska
- **Keywords**: QHyper, Quantum Optimization, Hyperparameter
Optimization, Variational Algorithms, Quantum Annealing, Penalties
- **Abstract**: We propose the QHyper library, which is aimed at researchers working on
computational experiments with a variety of quantum combinatorial optimization solvers. The library offers a simple and extensible interface for formulating combinatorial optimization problems, selecting and running solvers,
and optimizing hyperparameters. The supported solver set includes variational gate-based algorithms, quantum annealers, and classical solutions.
The solvers can be combined with provided local and global (hyper)optimizers.
The main features of the library are its extensibility on different levels of use
as well as a straightforward and flexible experiment configuration format presented in the paper.
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---

### Paper 15 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [FOCQS: Feedback Optimally Controlled Quantum States](https://arxiv.org/pdf/2409.15426)
- **Authors**: Lucas T. Brady, and Stuart Hadfield1
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---
### Paper 15 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [Solving Max-3SAT Using QUBO Approximation](https://arxiv.org/pdf/2409.15891)
- **Authors**: Sebastian Zielinski
- **Keywords**: Quadratic Unconstrained Binary Optimization,
Combinatorial Optimization, Max-3SAT, Approximation
- **Abstract**: As contemporary quantum computers do not possess
error correction, any calculation performed by these devices can
be considered an involuntary approximation. To solve a problem
on a quantum annealer, it has to be expressed as an instance
of Quadratic Unconstrained Binary Optimization (QUBO). In
this work, we thus study whether systematically approximating
QUBO representations of the MAX-3SAT problem can improve
the solution quality when solved on contemporary quantum hardware, compared to using exact, non-approximated QUBO representations. For a MAX-3SAT instance consisting of a 3SAT formula with n variables and m clauses, we propose a method
of systematically creating approximate QUBO representations of
dimension (n×n), which is significantly smaller than the QUBO
matrices of any exact, non-approximated MAX-3SAT QUBO
transformation. In an empirical evaluation, we demonstrate
that using our QUBO approximations for solving MAX-3SAT
problems on D-Wave’s quantum annealer Advantage System6.4
can yield better results than using state-of-the-art exact QUBO
transformations. Furthermore, we demonstrate that using naive
QUBO approximation methods, based on removing values from
exact (n + m) × (n + m)-dimensional QUBO representations of
MAX-3SAT instances, is ineffective.
- **Summary**: LUSION
Due to the missing error correction of contemporary quantum hardware, any quantum computer calculation can be
considered an involuntary solution approximation. In this
work, we thus studied whether it is possible to improve the
solution quality when solving problems on D-Wave’s quantum
annealer Advantage System6.4 by using systematic QUBO
approximation of MAX-3SAT problems instead of exact, nonapproximated QUBO representations as an input for the quantum annealer. For a MAX-3SAT instance consisting of a 3SAT
formula with n variables and m clauses, our proposed QUBO
approximation method yields (n × n)-dimensional QUBO
matrices, which is considerably smaller than the QUBO matrices that result from any exact, non-approximated QUBO
transformation. The method is based on an adaption of the
creation method of exact QUBO transformations that result
in QUBO matrices of dimension (n + m) × (n + m). In
an empirical evaluation, we demonstrated that our QUBO
approximations can yield comparable or even better results
than exact, non-approximated QUBO transformations when
solved on D-Wave’s quantum annealer Advantage System6.4.
Furthermore, 50% larger MAX-3SAT instances can be solved
on the quantum annealer due to our approximation method’s
reduced need for physical qubits. Additionally, we empirically
showed that naive methods of creating QUBO approximations
for MAX-3SAT problems using (n+m)×(n+m)-dimensional
QUBO matrices as initial QUBOs are not effective.
- **Miscellaneous**: Any additional information
---
### Paper 15 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---
### Paper 15 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
- **Miscellaneous**: Any additional information
---
### Paper 15 (Add more as needed)
- **Date**: 2024-09-28
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
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
---

### Paper I (Add more as needed)
- **Date**: YYYY-MM-DD
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
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
---

### Paper I (Add more as needed)
- **Date**: YYYY-MM-DD
- **Title**: [Title of the Paper](link)
- **Authors**: Author Names
- **Keywords**: List of keywords
- **Abstract**: Abstract text here
- **Summary**: Brief summary or key points of the paper
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

