"""
Unit and regression test for the MonteCarlo package.
Tests are taken from professor Mayhall's package in interest of time and matching
"""

# Import package, test suite, and other packages as needed
import sys
import numpy as np
import random
import MonteCarlo


def test_MonteCarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "MonteCarlo" in sys.modules

def test_average_values():
    N = 10
    str = ""
    for i in range(N):
        str += '0'
    conf = MonteCarlo.BitString(str)
    #conf.initialize(M=20)

    T = 2.0

    
    # now test the general ising hamiltonian
    Jval = 1.0
    mu = [.1 for i in range(N)]
    J = []
    for i in range(N):
        J.append([((i+1) % N, Jval), ((i-1) % N, Jval)])
    print(J)
    ham2 = MonteCarlo.IsingHamiltonian(J=J, mu=mu)
    E, M, HC, MS = ham2.compute_average_values(conf, T) 
 
    assert(np.isclose(E, -4.6378514858094695))
    assert(np.isclose(M, -0.1838233606011354 ))
    assert(np.isclose(HC, 1.9883833749653714 ))
    assert(np.isclose(MS, 1.8391722085614428))


def test_metropolis():
    random.seed(2)
    N=20
    str = ""
    for i in range(N):
        str += '0'
    conf = MonteCarlo.BitString(str)
    T = 2

    J = []
    Jval = 1.0
    mu = [.1 for i in range(N)]
    for i in range(N):
        J.append([((i+1) % N, Jval), ((i-1) % N, Jval)])
    ham = MonteCarlo.IsingHamiltonian(J=J, mu=mu)

    conf = MonteCarlo.BitString(str)
    E, M, EE, MM = MonteCarlo.metropolis_montecarlo(ham, conf, temp=T, nsweep=8000, nburn=1000)
    HC = (EE[-1] - E[-1]*E[-1])/T/T
    MS = (MM[-1] - M[-1]*M[-1])/T
    #print
    print("     E:  %12.8f" %(E[-1]))
    print("     M:  %12.8f" %(M[-1]))
    print("     HC: %12.8f" %(HC))
    print("     MS: %12.8f" %(MS))

    assert(np.isclose(-9.31, E[-1], 1))