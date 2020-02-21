from multiprocessing import Manager, Pool
from modules.sorting import merge_sort_recursive, merge_sort_iterative, append_sorted_list, append_merged_lists
from modules.helpers import generate_random_int_list, generate_random_float_list
from modules.timing import function_timing
from contextlib import contextmanager
import matplotlib.pyplot as plt
import time

@contextmanager
def create_pool(threads):
    pool = Pool(threads)
    yield pool
    pool.close()
    pool.join()

def threaded_merge_sort(function, array, threads):
    
    # if no threads, return normal merge sort results and timing
    if threads == 0:
        return function(array), function_timing(function, 1, array)
    
    else:
        # Create multiprocessing objects and start timer
        start = time.time()
        thread_manager = Manager()
        result_manager = thread_manager.list()

        # Add asynchronous processes to pool
        with create_pool(threads) as pool:
            for i in range(threads):
                pool.apply_async(append_sorted_list, (function, result_manager, array[i::threads]))

        # Merge sorted lists back into one sorted list
        while len(result_manager) > 1:
            with create_pool(threads) as pool:
                pool.apply_async(append_merged_lists, (result_manager, result_manager.pop(0), result_manager.pop(0)))
        
        # Merge sort higher dimensional list with module merge from heapq
        return result_manager[0], (time.time() - start)

if __name__ == '__main__':
    
    array_sizes = [10000, 10000]
    for array_length in array_sizes:
        # Test array
        array = generate_random_int_list(array_length)

        # Timings
        results = {'recursive': [], 'iterative': []}
        for i in [0, 1, 2, 4, 8]:
            sorted_array_recursive, timing_recursive = threaded_merge_sort(merge_sort_recursive, array, i)
            sorted_array_iterative, timing_iterative = threaded_merge_sort(merge_sort_iterative, array, i)
            results['recursive'].append(timing_recursive)
            results['iterative'].append(timing_iterative)
            print(f"{i} thread(s): \n\
                Timing in seconds (iterative): {str(timing_iterative)} | Verify: {sorted_array_iterative == sorted(array)}\n\
                Timing in seconds (recursive): {str(timing_recursive)} | Verify: {sorted_array_recursive == sorted(array)}\n")


        # Plot timings for iterative and recursive functions
        plt.figure(figsize=(14, 7))
        plt.title(f"Array size {str(array_length)}")
        for i in results:
            plt.xlabel("number of threads")
            plt.ylabel("runtime in seconds")
            plt.plot(list(range(1, len(results[i])+1)), results[i])
        plt.legend(list(results.keys()), loc='upper left')
        plt.show()