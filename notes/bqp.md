# Bounder error quantum polynomial time (BQP)
[Link](https://medium.com/@saarbk/the-frontiers-of-quantum-computing-complexity-classes-and-the-relation-between-bqp-and-np-cfdcd74ace68#:~:text=If%20BQP%20=%20NP%2C%20it%20would,range%20of%20industries%20and%20fields.)

Clearly, P ⊆ NP, but the above asks if P = NP. This is known as the P vs NP problem and it is considered one of the most important open problems in theoretical computer science. A solution to this problem would give The solver a $1M prize since P vs NP is mentioned as one of the Millennium Prize Problems (it is widely believed that P ≠ NP)

PSPACE stands for “polynomial space” and it represents the class of problems that can be solved using a polynomial amount of space on a classical computer. It is a complexity class that contains both P and NP, and it is considered a larger class than both of them. In other words, any problem that can be solved in polynomial time or polynomial space is also a PSPACE problem.

[pspace](../pspace.png)
Another interesting concept is the Time Hierarchy Theorem, which states that for any complexity class, there exists a problem that can be solved in a time that grows faster than a polynomial function. In simpler terms, it means that there is no upper limit to how complex a problem can be, and it is not known where the hierarchy collapses in the above diagram.

## Quantum Complexity Classes
<hr/>

**bounder-error polynomial time**: class of problems that can be solved on a quantum computer in polynomial time with a bounded probability of error. This class of problems is considered to be the “sweet spot” for quantum computing, as it represents a balance between the power and limitations of quantum computing, in particular with an error probability of at most 1/3 for all instances.

One of the most important and well-known problems in BQP is Shor’s algorithm, which is a quantum algorithm for factoring integers. It is exponentially faster than the best-known classical algorithm for this task.
Another important problem in BQP is the Quantum Approximate Optimization Algorithm (QAOA), which is a quantum algorithm for solving optimization problems. It has been shown to be more efficient than classical algorithms for certain types of optimization problems and has potential applications in fields such as machine learning and logistics.

**P ⊆ BQP**
Now let’s go back to the Complexity Hierarchy [1] shows that every classical circuit can be simulated by a quantum circuit, thus given a classical instant of a P problem we can generate an equivalent quantum circuit i.e. P ⊆ BQP. In terms of Time Complexity, let's give an upper bound for BQP. We begin with an easier containment BQP ⊆ EXP-SPACE, and then we will give a tighter bound BQP ⊆ P-SPACE, since P-SPACE ⊆ EXP-SPACE.
