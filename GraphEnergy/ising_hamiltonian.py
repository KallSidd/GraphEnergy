import numpy as np

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

    def compute_average_values(self, config, temp):
        # Z is the sum over all possible configurations
        Z = 


