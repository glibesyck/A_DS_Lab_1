"""
Module which implements Merge Sort of an array of n elements.
Time complexity - O(n*log(n)).
"""

def merge_sort(elements: list)-> list:
    """
    Return the sorted list of elements using MergeSort.
    """
    comparisons = 0
    if len(elements) <= 1:
        return elements, comparisons
    else:
        middle = len(elements)//2
        first_list = elements[:middle]
        second_list = elements[middle:]
        first_part = merge_sort(first_list)
        second_part = merge_sort(second_list)
        comparisons += first_part[1] + second_part[1]
        first_idx = second_idx = third_idx = 0
        while (first_idx < len(first_list)) and (second_idx<len(second_list)):
            comparisons += 1 #comp
            if first_list[first_idx] < second_list[second_idx]:
                elements[third_idx] = first_list[first_idx]
                first_idx+=1
            else:
                elements[third_idx] = second_list[second_idx]
                second_idx+=1
            third_idx+=1
        while(first_idx<len(first_list)):
            elements[third_idx] = first_list[first_idx]
            first_idx+=1
            third_idx+=1
        while (second_idx<len(second_list)):
            elements[third_idx] = second_list[second_idx]
            second_idx+=1
            third_idx+=1
        return elements, comparisons
