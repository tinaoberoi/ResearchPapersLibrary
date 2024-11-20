Why is Fermi Hubbard Model considered complex?

-  involves strongly correlated electrons on a lattice, leading to complex many-body quantum states
-  Understanding these states, especially in the presence of strong correlations and interactions, is difficult because of the exponential growth of the Hilbert space with the number of particles and lattice sites
-  this is quantun many body systems

Why is skyrmion challenging?
- Skyrmions are topologically protected spin textures that can emerge in certain magnetic materials.
- The challenge in studying Skyrmions lies in their topological nature, which requires understanding how these structures behave in the presence of external fields, thermal fluctuations, and interactions with other Skyrmions.
- quantum spin model

What is the difference between quantum spin model vs quantum many body problems?

**Quantum Spin models**
- Quantum spin models specifically describe systems of quantum spins (usually represented by spin-1/2 particles) on a lattice or in a defined spatial arrangement.
- The primary focus is on the interactions between these spins, which can include nearest-neighbor interactions, long-range interactions, and external fields.
- The Hamiltonians of quantum spin models are typically written in terms of spin operators (e.g., 𝑆𝑥, 𝑆𝑦, 𝑆𝑧) and include terms like the Ising model, Heisenberg model, and XY model.
- The Hamiltonian typically involves spin operators, with interactions that may include exchange interactions (e.g., in the Heisenberg model: 𝐻 = 𝐽 ∑ ⟨𝑖,𝑗⟩𝑆𝑖⋅𝑆𝑗), anisotropy, and external magnetic fields.
- The models often assume that the particles are localized, meaning they are fixed on lattice sites and don't have a spatial degree of freedom associated with movement.
- Quantum spin models are often used to study magnetism, quantum phase transitions, and entanglement in spin systems.

**Quantum Many Body Systems**
- Quantum many-body systems refer to a broader class of systems involving a large number of interacting quantum particles, which could be spins, bosons, fermions, or other types of particles.
- The Hamiltonians of quantum many-body systems can include a variety of terms, not limited to spin interactions but also incorporating kinetic energy (e.g., hopping terms), potential energy, and interaction terms among particles.
- The Hamiltonian is more general and can include terms beyond spin interactions, such as kinetic energy (e.g., hopping terms $𝑡∑⟨𝑖,𝑗⟩𝑐_𝑖^{†}c_j$), interaction energy (e.g., Coulomb interaction in electrons), and potential energy.
- These systems may involve delocalized particles, meaning the particles can move across the lattice or space, leading to phenomena like band structure and superconductivity.
- Examples include the Fermi-Hubbard model, Bose-Hubbard model, and lattice gauge theories.
- These systems are used to study emergent phenomena like superfluidity, superconductivity, topological phases, and quantum entanglement in large systems.
  
**Quantum Skyrmions**

A Hamiltonian to describe a system where skyrmions exist. Skyrmions are stable, characterised by a swirling arrangement of spins that cannot be deformed into trivial configuration without discontinuity. (Why break swirling pattern? eg: studying phase transitions between distinct states). These structures are topologically protected, meaning they are robust against perturbations like impurities or thermal fluctuations.

*Spin-Orbit Coupling:* A critical feature is the Dzyaloshinskii-Moriya Interaction (DMI), which arises due to strong spin-orbit coupling and stabilizes skyrmion structures. This term ensures that neighboring spins prefer a specific twisted configuration.

Comparison :

*Antiferromagnetic*
- Spins align parallel to minimize energy
  
$H = -J\sum S_iS_j$
(with J > 0)
- No topological textures; uniform magnetization

*Ferromagnetic*
- Spin aligns anti parallel to minimize energy
$H = -J\sum S_iS_j$
(with J < 0)
- Can exhibit checkboard like structure but still lack topological textures like skyrmions

*Quantum skyrmions*
- stabalised by DMI terms
- Quantum skyrmions can tunnel between different configurations, unlike classical counterparts. (which need barrier energy to transition, but quantum skyrmions can transition using quantum tunneling)

Where are skyrmions used?

- Spintronics data storage
- Quantum skyrmions can be created, moved, or annihilated using small energy inputs, enabling the development of energy-efficient computational technologies.

**NOTE**

Topological Constraints: While skyrmions are topologically protected, their annihilation requires specific conditions:
Boundary Annihilation: A skyrmion can be driven to the edge of the magnetic material, where it "unwinds" and disappears.
Pair Annihilation: A skyrmion can annihilate with an anti-skyrmion (a topological counterpart with opposite skyrmion number), resulting in a net zero topological charge.
External Fields or Currents: Applying a strong enough magnetic field or current can provide sufficient energy to destabilize the skyrmion and collapse its topological structure.