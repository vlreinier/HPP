#!/usr/bin/env python
import time
from mpi4py import MPI
import sys
from sympy import primerange
import pymp
import numpy as np

if __name__ == '__main__':

    # N argument must be given
    if len(sys.argv) > 1:
        
        # Initiate MPI variables
        comm = MPI.COMM_WORLD
        cores = comm.Get_size()
        rank = comm.Get_rank()
        N = int(sys.argv[1]) + 1
        if len(sys.argv) > 2:
                num_threads = int(sys.argv[2])
        else:
            num_threads = 1

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

        # Create empty local sieve
        sieve = pymp.shared.array((N,), dtype=bool)
        sieve[0] = True   # set non primes to True
        sieve[1] = True   # set non primes to True

        K = 2
        while K <= N**0.5:
            
            with pymp.Parallel(num_threads) as p:
                for i in p.range(max(start, K**2), end):
                    if i % K == 0:
                        sieve[i] = True   # set non primes to True

            if rank == 0:
                for i in range(K+1, N): 
                    if not sieve[i]:
                        K = i
                        break
            
            K = comm.bcast(K, root=0)

        # Gather and combine all local primes
        all_primes = comm.gather(sieve, root=0)
        
        # Print results
        if rank == 0:
            results = all_primes[0]
            for i in all_primes[1:]:
                for j in range(len(i)):
                    if i[j]:
                        results[j] = True
            results = [i for i in range(len(results)) if not results[i]]
            end_time = time.time()
            verify_results = list(primerange(0, N))
            print("\nN: " + str(N-1))
            print("Length comparison: {} == {} = {}".format(str(len(results)),
                str(len(verify_results)), str(len(results) == len(verify_results))))
            print("Result comparison: " + str(results == verify_results))
            print("Runtime: {:f} seconds\n".format(end_time - start_time))

    else:
        print("Please provide argument for N number of primes!")