"""
Module which implements Selection Sort of an array of n elements.
"""

def selection_sort(elements: list) -> list:
    """
    Return the sorted list of elements using SelectionSort.
    """
    comparisons = 0 #comp
    for i in range(len(elements)):
        min_idx = i
        for j in range(i + 1, len(elements)):
            comparisons += 1 #comp
            if elements[j] < elements[i]:
                min_idx = j
        elements[min_idx], elements[i] = elements[i], elements[min_idx]
    return elements, comparisons
