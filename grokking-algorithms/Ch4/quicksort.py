import random

#warmup
def sum(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum(l[1:])


print("Recursive sum = {}".format(sum([1,2,3,4,5,10,30])))


def count_list_elem(l):
    if len(l) == 0:
        return 0
    else:
        return 1 + count_list_elem(l[1:])


print("Recursive length of the list is {}".format(count_list_elem([1,2,3,4,5,6,7,8])))


def find_biggest_num(l):
    if len(l) == 0:
        return 0

    num = find_biggest_num(l[1:])
    if l[0] > num:
        return l[0]
    else:
        return num


print("Biggest num in the list {}".format(find_biggest_num([1,2,3,44,3,112,1])))


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[random.randrange(0, len(arr))]
    left = [i for i in arr[0:] if i < pivot]
    right = [i for i in arr[0:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


l = list(range(0, 100))
random.shuffle(l)

print(l)
sorted_arr = quicksort(l)
print(sorted_arr)