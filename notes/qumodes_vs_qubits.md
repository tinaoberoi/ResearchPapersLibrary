Qumodes vs qubits
![Source](https://quixquantum.medium.com/qumodes-vs-qubits-explained-part-i-a5ea4e252ca7)


Photonic processors uses qumodes, which are a different way of carrying and manipulating quantum information than qubits. 

**States of qubits**

In case of qubits we have 2 basis (up and down spin), using these basis I can express every other state. Thus each qubit has 2 possible arrangements. So if I have n of them, possible states are $2^n$ possible states.

**States of qumodes**

A qumode is a quantum mechanical harmonic osscilator. And we take this harmonic osscilator and make the system small enough such that the quantum mechanics begings to play a role. Then we will notice that such a system has discrete quantum states. It is these states which we will use to encode our information.
(Quix case:)
In our case the qumode is light, and this single beam of light is a harmonic oscialltor. For this case, states can be thoughts of as corresponding to a given number of photons (particles of light). If you bring two qumodes in contact with each other, then photons can jump from one qumode to the other. If the engineering has been done properly, then this can happen without any photons getting lost, i.e. being absorbed or flying out of the system. If there are photons in both qumodes, then generally such an interaction results in entanglement, i.e. in a joint state between the two qumodes.

Now, we can look at the state space of qumodes. Let’s begin with a single qumode. Unlike qubits, the basis of a single qumode contains infinitely many states, since the qumode can contain an arbitrary number of photons. However in practice, a photonic processor will always be run with some states with a finite energy, meaning that there is a limit on the number photons that can be present (because making a photon costs energy).

Lets assume we have fixed and finite number of photons in our qumodes. In that case, the only choice we have to make is how to put these photons among the qumodes. It turns out if there are N qumodes, and n photons there are $\C^{{N+n-1}}_{n}$ number of ways to do this. (In qubit case it was $2^n$).

This highlights the important difference between qumodes and qubits: The way their state spaces are structures is completely different. Thus there isnt a one-one equivalence between qumodes and qubits.
