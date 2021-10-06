"""
Module which implements Insertion Sort of an array of n elements.
"""

def insertion_sort(elements: list) -> list:
    """
    Return the sorted list of elements using InsertionSort.
    """
    comparisons = 0 #comp
    for i in range(1, len(elements)):
        key_elem = elements[i]
        idx = i - 1
        while idx >= 0 and elements[idx] > key_elem:
            elements[idx], elements[idx+1] = elements[idx+1], elements[idx]
            idx -= 1
            comparisons += 1 #comp
        comparisons += 1 #comp
    return elements, comparisons
