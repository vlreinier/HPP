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

        # Create sieve
        sieve = []

        # Finding primes
        while start <= end ** 0.5:

            for i in range(start**2, end):
                if i % start == 0:
                    sieve[i] = False

            for i in range(sieve.index(start), len(sieve)):
                k = sieve[i]
                if k:
                    start = k
                    break

        # Extracting
        results = []
        for i in sieve:
            if i:
                results.append(i)
        #print(results)

        out = comm.gather(results, root=0)
        
        if rank == 0:
            data = sorted([j for i in out for j in i])
            print(data)
            print(len(data))
            print(data == list(primerange(0, N)))
            print(time.time() - start_time)

    else:
        print("Please provide argument for N number of primes!")