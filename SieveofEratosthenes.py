#!/usr/bin/env python
import pymp
import timeit
from mpi4py import MPI


def function_timing(function, repeat=1, **kwargs):
    return timeit.timeit(lambda: function(**kwargs), number=repeat)


def Sieve_Of_Eratosthenes(N):

    rank = comm.Get_rank()
    if rank == 0:
        print('\nSieve of Eratosthenes in parallel\nUsed MPI processes: {}\n'.format(cores))
    print(rank)

    """
    Lists in Python are thread safe, although is does not really
    matter if values are updated at the same time,
    because they can only be changed to False
    """
    sieve = [True for i in range(N + 1)]  # include N
    sieve[0] = False
    sieve[1] = False

    k = 2
    while k ** 2 <= N:
        
        for i in range(k ** 2, N + 1):
            if i % k == 0:
                sieve[i] = False
                
        for i in range(k + 1, N + 1):
            if sieve[i]:
                k = i
                break

    results = []
    for i in range(N + 1):
        if sieve[i]:
            results.append(i)

    return results


if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    cores = comm.Get_size()

    print(Sieve_Of_Eratosthenes(29))