import MonteCarlo.ising_hamiltonian as ising_ham
import numpy as np

def get_next(list, index, value):
    return (list[index - 1] * index + value) / (index + 1)

def metropolis_montecarlo(ham: ising_ham.IsingHamiltonian, config, temp=1.0, nsweep=1000, nburn=100):
    for i in range(nburn):
        ham.metropolis_sweep(config, temp)
    
    energy_list = np.zeros(nsweep)
    magnetization_list = np.zeros(nsweep)
    e_energy_list = np.zeros(nsweep)
    m_magnetization_list = np.zeros(nsweep)
    
    energy_list[0] = ham.energy(config)
    magnetization_list[0] = ham.get_spin_diff(config)
    e_energy_list[0] = ham.energy(config) ** 2
    m_magnetization_list[0] = ham.get_spin_diff(config) ** 2

    for j in range(1, nsweep):
        ham.metropolis_sweep(config, temp)

        energy_list[j] = get_next(energy_list, j, ham.energy(config))
        magnetization_list[j] = get_next(magnetization_list, j, ham.get_spin_diff(config))
        e_energy_list[j] = get_next(e_energy_list, j, ham.energy(config) ** 2)
        m_magnetization_list[j] = get_next(m_magnetization_list, j, ham.get_spin_diff(config) ** 2)
    
    return energy_list, magnetization_list, e_energy_list, m_magnetization_list
