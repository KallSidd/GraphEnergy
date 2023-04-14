import numpy as np
import bitstring as bs

class IsingHamiltonian:
    
    def __init__(self, J=[[()]], mu=np.zeros(1)):
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
        if(len(config) != len(self.J)):
            raise Exception("Invalid config size")

        sum = 0
        spin1 = 1
        spin2 = 1
        for i in self.J:
            if(str(config)[i] == '1'):
                spin1 = 1
            else:
                spin1 = -1
            
            sum += self.mu[i] * spin1

            for j in self.J[i]:
                if(str(config)[j[0]] == '1'):
                    spin2 = 1
                else:
                    spin2 = -1
                sum += spin1 * spin2 * j[1]
        return sum

    def compute_average_values(self, config, temp):
        M = 0.0
        E = 0.0
        
        bitstring = bs.BitString([0]*len(config))

        def get_spin_diff(config):
            spin_diff = 0
            for i in range(len(config)):
                if(str(config[i]) == '1'):
                    spin_diff += 1
                else:
                    spin_diff -= 1
            return spin_diff
        
        def config_probablity(config, len):
            Z = 0.0
            for i in range(0, 2**(len(config))):
                Z += np.exp(-self.energy(bitstring) / temp)
                config.set_int(i, len)

            return (1 / Z) * np.exp(-self.energy(config) / temp)

        for i in range(0, 2**len(config)):
            M += get_spin_diff(config) * config_probablity(config, len(config))
            E += self.energy(config) * config_probablity(config, len(config))

        
