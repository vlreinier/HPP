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

        sieve = set()
        for K in range(2, int(N**0.5) + 1):
            for i in range(max(start, K**2), end):
                if i % K == 0:
                    sieve.add(i)
            
        all_primes = comm.gather([i for i in range(start, end) if not i in sieve], root=0)
        
        if rank == 0:
            data = [j for i in all_primes for j in i]
            #print(data)
            print(len(data))
            print(data == list(primerange(0, N)))
            print(time.time() - start_time)

    else:
        print("Please provide argument for N number of primes!")