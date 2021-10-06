"""
Module which implements Shell Sort of an array of n elements.
"""

def shell_sort(elements: list) -> list:
    """
    Return the sorted list of elements using ShellSort.
    IMPORTANT: we will use the formula to find the interval interval 1, 4, 13 and so on, (3x+1).
    """
    comparisons = 0 #comp
    curr_interval = 1
    while len(elements)//3 > curr_interval:
        curr_interval = 3*curr_interval + 1
    while curr_interval >= 1:
        for i in range(curr_interval-1, len(elements)):
            pivot = elements[i]
            idx = i
            while idx >= curr_interval and pivot < elements[idx - curr_interval]:
                comparisons+=1 #comp
                elements[idx] = elements[idx - curr_interval]
                idx -= curr_interval
                elements[idx] = pivot
            comparisons +=1
        curr_interval = (curr_interval-1)//3
    return elements, comparisons
