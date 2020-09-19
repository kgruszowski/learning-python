import random

def find_smallest_index(arr):
    smallest_index = 0
    smallest_element = arr[0]

    for i in range(0, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    for i in range(0, len(arr)):
        lowest = i + find_smallest_index(arr[i:])
        j = arr[i]
        arr[i] = arr[lowest]
        arr[lowest] = j

    return arr

l = list(range(0,100))
random.shuffle(l)

print(l)
sorted_arr = selection_sort(l)
print(sorted_arr)