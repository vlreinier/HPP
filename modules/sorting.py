from typing import List

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

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort_recursive(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort_recursive(array[:half])
    right = merge_sort_recursive(array[half:])

    return merge(left, right)

def merge_sort_iterative(array) -> None:

    unit = 1

    while unit <= len(array):

        h = 0

        for h in range(0, len(array), unit * 2):

            l, r = h, min(len(array), h + 2 * unit)
            mid = h + unit
            p, q = l, mid

            while p < mid and q < r:
                if array[p] <= array[q]:
                    p += 1
                else:
                    tmp = array[q]
                    array[p + 1: q + 1] = array[p:q]
                    array[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2

    return array


def append_sorted_list(function, result_manager, array):
    return result_manager.append(function(array))

def append_merged_lists(result_manager, left, right):
    return result_manager.append(merge(left, right))