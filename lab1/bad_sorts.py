"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""

import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

LENGTHS = [1000, 2000, 10000]

insertion_times = [
    np.mean([0.0222, 0.0204, 0.0210, 0.0195, 0.0215], dtype=np.float32),  # 1000
    np.mean([0.0734, 0.0682, 0.0749, 0.0748, 0.0736], dtype=np.float32),  # 2000
    np.mean([1.6738, 1.6754, 1.6500, 1.6712, 1.7030], dtype=np.float32),  # 10000
]

bubble_times = [
    np.mean([0.0356, 0.0315, 0.0388, 0.0421, 0.0388], dtype=np.float32),  # 1000
    np.mean([0.1276, 0.1342, 0.1260, 0.1281, 0.1340], dtype=np.float32),  # 2000
    np.mean([3.2044, 3.3141, 3.2322, 3.3433, 3.3385], dtype=np.float32),  # 10000
]

selection_times = [
    np.mean([0.0104, 0.0129, 0.0094, 0.0130, 0.0105], dtype=np.float32),  # 1000
    np.mean([0.0342, 0.0426, 0.0418, 0.0410, 0.0406], dtype=np.float32),  # 2000
    np.mean([0.8183, 0.8190, 0.8497, 0.8090, 0.8198], dtype=np.float32),  # 10000
]

plt.plot(
    LENGTHS,
    insertion_times,
    marker="o",
    color="#4c72b0",
    mfc="#4c72b0",
    label="Insertion Sort",
)

plt.plot(
    LENGTHS,
    bubble_times,
    marker="o",
    color="#c44e52",
    mfc="#c44e52",
    label="Bubble Sort",
)

plt.plot(
    LENGTHS,
    selection_times,
    marker="o",
    color="#55a868",
    mfc="#55a868",
    label="Selection Sort",
)
plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.title("Bad Sorting Algorithms Comparison")
plt.tight_layout()

plt.show()


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************


# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    start = timeit.default_timer()
    for i in range(1, len(L)):
        insert(L, i)
    elapsed = timeit.default_timer()

    return elapsed - start


def insert(L, i):
    while i > 0:
        if L[i] < L[i - 1]:
            swap(L, i - 1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    start = timeit.default_timer()
    for i in range(1, len(L)):
        insert2(L, i)
    elapsed = timeit.default_timer()
    return elapsed - start


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# print(insertion_sort2(create_random_list(10000, 50)))


# ******************* Bubble sort code *******************


# Traditional Bubble sort
def bubble_sort(L):
    start = timeit.default_timer()
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)
    elapsed = timeit.default_timer()
    return elapsed - start


# print(bubble_sort(create_random_list(10000, 50)))


# ******************* Selection sort code *******************


# Traditional Selection sort
def selection_sort(L):
    start = timeit.default_timer()
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)
    elapsed = timeit.default_timer()

    return elapsed - start


def find_min_index(L, n):
    min_index = n
    for i in range(n + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# print(selection_sort(create_random_list(10000, 50)))
