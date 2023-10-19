#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

import random
import csv

print ("Content-type: text/html\n")

# Quicksort and Partition functions implemented are similar
# to both Hackerrank and CSC220 Textbook inplace_quick_sort.py

def quickSort(arr, a, b): # replaced S to arr for my better understanding
    count = 0
    if (a >= b):            # Constraint
        return count 
    pivot = arr[b]          # last element of range is pivot
    left = a                # will scan rightward
    right = b - 1           # will scan leftward
    while (left <= right):
        # scan until reaching value >= to pivot (right marker)
        while (left <= right and arr[left] < pivot):
            left += 1
        # scan until reaching value <= to pivot (left marker)
        while (left <= right and pivot < arr[right]):
            right -= 1
        if (left <= right): # scans did not strictly cross
            arr[left], arr[right] = arr[right], arr[left] # swap values
            left, right = left + 1, right - 1 # shring range
    # put pivot into its final place (currently marked by left index)
    arr[left], arr[b] = arr[b], arr[left]
    count += 1
    # make recursive calls
    count += quickSort(arr, a, left - 1)
    count += quickSort(arr, left + 1, b)
    return count

# Insertion Sort Method for Extra Credit Below
def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        count += 1
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return count

# Testing quickSort function with imports
# Using methods similar to ones I used in project03

# Method that creates random data points
def dataPointGenerator(data_size):
    random_data = [random.randint(1, 10000) for i in range(data_size)]
    times_visited_quicksort = quickSort(random_data, 0, len(random_data) - 1)
    times_visited_insertionsort = insertionSort(random_data)
    return data_size, times_visited_quicksort, times_visited_insertionsort
# Method that stores random data points
def storeData(points):
    data_points = []
    for i in range(points):
        data_size = random.randint(1000, 10000)
        data_points.append(dataPointGenerator(data_size))
    return data_points
# Method to save data to csv file
def saveToCSV(data_points, fileName):
    with open(fileName, 'w') as csvfile:
        graphFile = csv.writer(csvfile)
        graphFile.writerow(['Data Size', 'Array Accesses'])
        # for loop to write in data automatically
        for d in data_points:
            graphFile.writerow(d)

# Conditionals??? I don't know what this is called but it writes out
# data needed as long as it's executed in main.py
if __name__ == '__main__':
    points = 500
    data_points = storeData(points)
    saveToCSV(data_points, 'quick_sort_and_insertion_sort.csv')
