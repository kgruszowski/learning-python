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
    sorted_arr = []
    for i in range(0, len(arr)):
        smallest_index = find_smallest_index(arr)
        sorted_arr.append(arr[smallest_index])
        del arr[smallest_index]

    return sorted_arr

l = list(range(0,100))
random.shuffle(l)

print(l)
sorted_arr = selection_sort(l)
print(sorted_arr)