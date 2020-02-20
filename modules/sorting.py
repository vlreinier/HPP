from typing import List
import time

def selection_sort(data: List[int]) -> None:
    """Sort an array using selection sort"""
    # loop over len(data) -1 elements
    for index1 in range(len(data)-1):
        smallest = index1 # first index of remaining array

        # loop to find index of smallest element
        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[index1]:
                smallest = index2

        # swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]


def recursive_selection_sort(data: List[int]) -> None:
    # Lists with less than one element are sorted
    if len(data) <= 1:
        return data
    else:
        smallest = min(data)    # find the smallest element in the list
        data.remove(smallest)   # remove from the list
        return [smallest] + recursive_selection_sort(data) # put on front of to be sorted remainder
    
def insertion_sort(data: List[int]) -> None:
    """Sorting an array in place using insertion sort."""
    # loop over len(data) - 1 elements
    for next in range(1, len(data)):
        insert = data[next] # value to insert
        move_item = next    # location to place element

        # search for place to put current element
        while move_item > 0 and data[move_item - 1] > insert:
            # shift element right one slot
            data[move_item] = data[move_item - 1]
            move_item -= 1

        data[move_item] = insert # place inserted element


def recursive_insertion_sort(toSort: List[int], sorted: List[int] = []) -> List[int]:
    """Recursive implementation of insertion sort"""
    if len(toSort) == 0: # empty lists are sorted
        return sorted
    else:
        head, *tail = toSort
        sorted = recursive_insertion(head, sorted) # insert the head into the sorted list
        return recursive_insertion_sort(tail, sorted) # recursive call to sort the remainder


def recursive_insertion(element: int, data: List[int]) -> List[int]:
    """Assistant function to recursive insertion sort; recursively insert into a list"""
    if len(data) == 0: # if the list is empty, the element should be place there anyway
        return [element]
    else:
        head, *tail = data
        if element < head: # when the element is smaller than the head of the insertion list
            return [element, head] + tail # place it on the front
        else:
            return [head] + recursive_insertion(element, tail) # else, keep the head separate, and recursively insert into the tail
        

def merge_sort(data: List[int]) -> None:
    merge_sort2(data, 0, len(data)-1)

def merge_sort2(data: List[int], low: int, high: int) -> None:
    """Split data, sort subarrays and merge them into sorted array."""
    # test base case size of array equals 1
    if (high - low) >= 1: # if not base case
        middle1 = (low + high) // 2 # calculate middle of the array
        middle2 = middle1 + 1 # calculate next element over

        # split array in half then sort each half (recursive calls)
        merge_sort2(data, low, middle1) # first half of the array
        merge_sort2(data, middle2, high) # second half of the array

        # merge two sorted arrays after split calls return
        merge(data, low, middle1, middle2, high)

# merge two sorted subarrays into one sorted subarray
def merge(data: List[int], left: int, middle1: int, middle2: int, right: int) -> None:
    left_index = left # index into left subarray
    right_index = middle2 # index into right subarray
    combined_index = left # index into temporary working array
    merged = [0] * len(data) # working array

    # merge arrays until reaching end of either
    while left_index <= middle1 and right_index < right:
        # place smaller of two current elements into result
        # and move to next space in arrays
        if data[left_index] <= data[right_index]:
            merged[combined_index] = data[left_index]
            combined_index += 1
            left_index += 1
        else:
            merged[combined_index] = data[right_index]
            combined_index += 1
            right_index += 1

    # if left array is empty
    if left_index == middle2: # if True, copy in rest of right array
        merged[combined_index:right + 1] = data[right_index:right + 1]
    else: # right array is empty, copy in rest of left array
        merged[combined_index:right + 1] = data[left_index: middle1 + 1]

    data[left:right + 1] = merged[left:right + 1] # copy back to data

def merge_sort_v2(data: List[int]) -> List[int]:
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              data[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                data[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k]=right[j]
            j += 1
            k += 1


def merge_sort_v3(xs) -> None:

    start = time.time()

    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            p, q = l, mid
            while p < mid and q < r:
                if xs[p] <= xs[q]:
                    p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2
    
    end = time.time() - start

    return xs, end


def append_sorted_list(result_manager, array):
    return result_manager.append(merge_sort_v3(array)[0])