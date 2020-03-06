#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{

  int var = 5;
  int numThreads = omp_get_num_threads();
  printf("%d\n", numThreads);

  #pragma omp parallel private(var)

  while (numThreads > 0)
  {
    var = var + omp_get_thread_num();
    printf("Hello World from thread: %d | var: %d\n", omp_get_thread_num(), var);
    numThreads--;
  }
}
