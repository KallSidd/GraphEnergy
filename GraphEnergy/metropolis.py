import ising_hamiltonian as ham

def metropolis_montecarlo(self, ham, config, temp=1, nsweep=1000, nburn=100):
    for i in range(nburn):
        ham.metropolis_sweep(config, temp)
    