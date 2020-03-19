#!/usr/bin/env python
import time
from mpi4py import MPI
import sys
from sympy import primerange

def is_prime(num):

    # Zero or one are never primes
    if num in [0, 1]:
        return False

    # Check if given num is a prime
    for j in range(2, num):
        if num % j == 0:
            return False

    return True

if __name__ == '__main__':

    # N argument must be given
    if len(sys.argv) == 2:
        
        # Initiate MPI variables
        comm = MPI.COMM_WORLD
        cores = comm.Get_size()
        rank = comm.Get_rank()
        N = int(sys.argv[1])

        # Initiate empty array to collect all primes from all processes
        if rank == 0:
            print("\n\nFinding primes with the sieve of Eratosthenes:")
            all_primes = []
            start_time = time.time()

        # Distribute work over processes using stripes
        local_primes = []
        for i in range(rank, N + 1, cores):
            if is_prime(i):
                local_primes.append(i)

        # Add locally found primes with all primes as nested list
        all_primes = comm.gather(local_primes, root=0)

        # Print results
        if rank == 0:
            result = sorted([j for i in all_primes for j in i])
            verification = list(primerange(0, N + 1))
            print("\nCorrect result: " + str(result == verification))
            print("Running time: {}\n\n".format(str(time.time() - start_time)))

    else:
        print("Please provide argument for N number of primes!")