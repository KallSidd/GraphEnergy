import numpy as np
import MonteCarlo.bitstring as bs
import random

class IsingHamiltonian:
    
    def __init__(self, J=[[()]], mu=list(np.zeros(1))):
        """ Constructor 
    
        Parameters
        ----------
        J: list of lists of tuples, optional
            Strength of coupling, e.g, 
            [(4, -1.1), (6, -.1)]
            [(5, -1.1), (7, -.1)]
        mu: vector, optional
            local fields 
        """
        self.J = J
        self.mu = mu

    def energy(self, config):
        """ Computes the energy of a given configuration
        
        Parameters
        ----------
        config: BitString
            input configuration
            
        Returns
        -------
        energy: float
            the energy of the given configuration
        """
        if(bs.BitString.__len__(config) != len(self.J)):
            raise Exception("Invalid config size")
        
        sum = 0
        spin1 = 1
        spin2 = 1
        for i in range(len(config)):
            if(str(config)[i] == '1'):
                spin1 = 1
            else:
                spin1 = -1
            
            sum += self.mu[i] * spin1

            for j in self.J[i]:
                if(j[0] < i):
                    if(str(config)[j[0]] == '1'):
                        spin2 = 1
                    else:
                        spin2 = -1
                    sum += spin1 * spin2 * j[1]
        return sum

    def get_spin_diff(self, config):
        spin_diff = 0
        for i in range(len(config)):
            if(str(config)[i] == '1'):
                spin_diff += 1
            else:
                spin_diff -= 1
        return spin_diff

    def compute_average_values(self, config, temp):
        """ Compute Average values exactly
        Parameters
        ----------
        conf   : :class:`BitString`
            input configuration 
        T      : int
            Temperature
        
        Returns
        -------
        E  : float 
            Energy
        M  : float
            Magnetization
        HC : float
            Heat Capacity
        MS : float
            Magnetic Susceptability
        """
        bitstring = bs.BitString([0]*len(config))
        Z = 0.0
        M = 0.0
        E = 0.0
        HC = 0.0
        MS = 0.0

        EE = 0.0
        MM = 0.0
        
        for i in range(2**len(config)):
            bitstring.set_int(i, len(config))
            
            # config changes here for some reason
            config_energy = self.energy(bitstring)
            Z_constant = np.exp(-config_energy / temp)
            E += config_energy * np.exp(-config_energy / temp)
            EE += config_energy**2 * np.exp(-config_energy / temp)
            M += self.get_spin_diff(bitstring) * np.exp(-config_energy / temp)
            MM += self.get_spin_diff(bitstring)**2 * np.exp(-config_energy / temp)
            Z += Z_constant

        E /= Z
        EE /= Z
        M /= Z
        MM /= Z

        HC = (EE - E**2) / (temp ** 2)
        MS = (MM - M**2) / temp

        return E, M, HC, MS
    
    def metropolis_sweep(self, config, temp=1.0):
        for i in range(len(config)):
            curr_energy = self.energy(config)
            config.flip(i)
            new_energy = self.energy(config)

            if(new_energy > curr_energy):
                keep_probability = np.exp(-(new_energy - curr_energy) / temp)

                if(random.random() >= keep_probability):
                    config.flip(i)

        return config