/* arraySum.c uses an array to sum the values in an input file,
 *  whose name is specified on the command-line.
 * Huib Aldewereld, HU, HPP, 2020
 */

#include <stdio.h>      /* I/O stuff */
#include <stdlib.h>     /* calloc, etc. */
#include <omp.h>

void readArray(char * fileName, double ** array, int * n);
double ompSumArray(double * array, int numValues, int threads);
double sumArray(double * array, int numValues, int threads);
double arraySumRuntime(double * array, int array_length, int threads, double (*function) (double *, int, int));

int main(int argc, char **argv)
{
  int  array_length;
  double * array;
  int threads_length = 5;
  int threads[] = {1, 2, 4, 8, 16};

  if (argc < 2) {
    fprintf(stderr, "\n*** Usage: arraySum <inputFile> <inputFile> etc..\n\n");
	  exit(1);
  }

  printf("%s", "\n");

  // get and print runtimes
  for (int i = 1; i < argc; i++) {

    readArray(argv[i], &array, &array_length);
    double seq = arraySumRuntime(array, array_length, threads[i], sumArray);
    printf("%s\nSequential: %f\n", argv[i], seq);

    for (int j = 0; j < threads_length; j++) {

      double omp = arraySumRuntime(array, array_length, threads[i], ompSumArray);
      printf("\tParallel: %f - Thread(s): %d\n", omp, threads[j]);

    }

    printf("%s", "\n");
    free(array);

  }

  return 0;
}

/* readArray fills an array with values from a file.
 * Receive: fileName, a char*,
 *          a, the address of a pointer to an array,
 *          n, the address of an int.
 * PRE: fileName contains N, followed by N double values.
 * POST: a points to a dynamically allocated array
 *        containing the N values from fileName
 *        and n == N.
 */

void readArray(char * fileName, double ** array, int * n) {
  int count, array_length;
  double * tempA;
  FILE * fin;

  fin = fopen(fileName, "r");
  if (fin == NULL) {
    fprintf(stderr, "\n*** Unable to open input file '%s'\n\n",
                     fileName);
    exit(1);
  }

  fscanf(fin, "%d", &array_length);
  tempA = calloc(array_length, sizeof(double));
  if (tempA == NULL) {
    fprintf(stderr, "\n*** Unable to allocate %d-length array",
                     array_length);
    exit(1);
  }

  for (count = 0; count < array_length; count++) {
    fscanf(fin, "%lf", &tempA[count]);
  }

  fclose(fin);
  *n = array_length;
  *array = tempA;
}

double arraySumRuntime(double * array, int array_length, int threads, double (*function) (double *, int, int)) {

  double start = omp_get_wtime();
  function(array, array_length, threads);
  double end = omp_get_wtime() - start;

  return end;
}

/* sumArray sums the values in an array of doubles.
 * Receive: a, a pointer to the head of an array;
 *          numValues, the number of values in the array.
 * Return: the sum of the values in the array.
 */

double sumArray(double *array, int numValues, int threads) {
  int i;
  double result = 0.0;

  for (i = 0; i < numValues; i++) {
	  result += array[i];
  }

  return result;
}

double ompSumArray(double * array, int numValues, int threads) {
  int i;
  double result = 0.0;
 
  #pragma omp parallel for reduction(+:result) num_threads(threads)
  for (i = 0; i < numValues; i++) {
    //#pragma omp atomic
    //#pragma omp critical
    result += array[i];
  }

  return result;
}
