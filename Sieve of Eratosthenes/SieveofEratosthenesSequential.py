#!/usr/bin/env python
import time
import sys
from sympy import primerange


if __name__ == '__main__':

    # N argument must be given
    if len(sys.argv) == 2:
        
        N = int(sys.argv[1]) + 1
        start_time = time.time()
        sieve = [True for i in range(N)]
        sieve[0] = False
        sieve[1] = False

        # Finding primes
        k = 2
        while k <= N**0.5:

            for i in range(k**2, N):
                if i % k == 0:
                    sieve[i] = False

            for i in range(k+1, N):
                if sieve[i]:
                    k = i
                    break

        # Extracting
        results = []
        for i in range(N):
            if sieve[i]:
                results.append(i)
        
        print(len(results))
        print(results == list(primerange(0, N)))
        print(time.time() - start_time)

    else:
        print("Please provide argument for N number of primes!")