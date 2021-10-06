"""
Main module for testing the time complexity of 4 different sort algorithms:
Inserion Sort, Merge Sort, Selection Sort and Shell Sort.
"""
from merge_sort import merge_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from insertion_sort import insertion_sort
from random import randint, choice
import time
import csv

POWERS = [7, 8, 9, 10, 11, 12, 13, 14, 15]
SORTS = [merge_sort, selection_sort, shell_sort, insertion_sort]
file = open("sorts.csv", "w")
writer = csv.writer(file)

def experiment_one(power: int) -> list:
    """
    Return 5 randomized arrays of 2^power elements.
    """
    array = []
    for _ in range(5):
        prob_array = []
        for _ in range (2**power):
            prob_array.append(randint(0, 2**power))
        array.append(prob_array)
    return array

def experiment_two(power: int) -> list:
    """
    Return the sorted in ascended array of 2^power elements.
    """
    array = []
    prob_array = []
    for i in range (2**power):
        prob_array.append(i)
    array.append(prob_array)
    return array

def experiment_three(power: int) -> list:
    """
    Return the sorted in descended array of 2^power elements.
    """
    array = []
    prob_array = []
    for i in range (2**power-1, -1, -1):
        prob_array.append(i)
    array.append(prob_array)
    return array

def experiment_four(power: int) -> list:
    """
    Return 3 arrays which consists only of elements 1, 2, 3.
    """
    array = []
    for _ in range(3):
        prob_array = []
        for _ in range (2**power):
            prob_array.append(choice([1, 2, 3]))
        array.append(prob_array)
    return array

EXPERIMENTS = [experiment_one, experiment_two, experiment_three, experiment_four]

def run():
    """
    Return 8 different graphics: 2 for each of the experiment above. First one is 
    the number of comparisons as y-axis and power of 2 which corresponds to the length
    of the array as x-axis; second one is the time as y-axis and power of 2 
    which corresponds to the length of the array as x-axis.
    """
    for experiment in EXPERIMENTS:
        for power in POWERS:
            arrays = experiment(power)
            for sort in SORTS:
                sum_time = 0
                comparisons = 0
                for array in arrays:
                    before = time.time()
                    comparisons += sort(array.copy())[1]
                    sum_time += time.time() - before
                sum_time = sum_time/len(arrays)
                comparisons = comparisons // len(arrays)
                writer.writerow([experiment.__name__, power, sort.__name__, sum_time, comparisons])

if __name__ == "__main__":
    run()
    file.close()
