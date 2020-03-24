#!/usr/bin/env python
import time
from mpi4py import MPI
import sys
from sympy import primerange


if __name__ == '__main__':

    # N argument must be given
    if len(sys.argv) == 2:
        
        # Initiate MPI variables
        comm = MPI.COMM_WORLD
        cores = comm.Get_size()
        rank = comm.Get_rank()
        N = int(sys.argv[1]) + 1

        # Record start time
        if rank == 0:
            start_time = time.time()

        # Range assigning
        part = N // cores
        remainder = N % cores
        start = rank * part
        end = start + part
        if rank + 1 == cores:
            end += remainder
        if start == 0:
            start = 2

        # Create empty local sieve
        sieve = set() 

        # Save non primes
        K = 2
        while K <= end**0.5:

            for i in range(max(start, K**2), end):
                if i % K == 0:
                    sieve.add(i)

            K+=1

        # Gather and combine all local primes
        all_primes = comm.gather([i for i in range(start, end) if not i in sieve], root=0)
        
        # Print results
        if rank == 0:
            results = [j for i in all_primes for j in i]
            end_time = time.time()
            verify_results = list(primerange(0, N))
            print("\nN: " + str(N-1))
            print("Length comparison: {} == {} = {}".format(str(len(results)),
                str(len(verify_results)), str(len(results) == len(verify_results))))
            print("Result comparison: " + str(results == verify_results))
            print("Runtime: {:f} seconds\n".format(end_time - start_time))

    else:
        print("Please provide argument for N number of primes!")