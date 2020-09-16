import math

def binary_search(set, number):

    steps = 0
    set_min = min(set)
    set_max = max(set)

    while set_min <= set_max:
        steps += 1
        guess = math.floor((set_min + set_max) / 2)
        print("Guess {}".format(guess))
        if set[guess] == number:
            print("You win - the number is {}".format(number))
            print("Number of steps {}".format(steps))
            return
        elif set[guess] > number:
            set_max = guess-1
        elif set[guess] < number:
            set_min = guess+1

    print("Number {} not found in the set".format(number))
    return None


binary_search(range(10000000), 4)