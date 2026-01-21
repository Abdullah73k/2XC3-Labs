"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""

import random
import timeit


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


def bubble_sort2(L):
    n = len(L)
    swapped = True

    while swapped:
        swapped = False
        i = 0

        while i < n - 1:
            value = L[i]

            j = i
            while j < n - 1 and value > L[j + 1]:
                L[j] = L[j + 1] 
                j += 1
                swapped = True

            L[j] = value  
            i = j + 1  

        n -= 1 

    return L


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


# Improved Selection sort
def selection_sort2(L):
    start = timeit.default_timer()
    n = len(L)
    for i in range(n // 2):
        start_index = i
        end_index = n - 1 - i
        
        min_index = start_index
        max_index = start_index

        for j in range(start_index, end_index + 1):
            if L[j] < L[min_index]:
                min_index = j
            if L[j] > L[max_index]:
                max_index = j
        
        swap(L, start_index, min_index)
        
        if max_index == start_index:
            max_index = min_index
            
        swap(L, end_index, max_index)

    elapsed = timeit.default_timer()
    return elapsed - start

print("Selection Sort 2", selection_sort2(create_random_list(10000, 50)))
