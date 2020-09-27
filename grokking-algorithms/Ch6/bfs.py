from _collections import deque

def is_target_letter(letter, target):
    if letter == target:
        return True

def look_for_letter(graph, target):
    visited = []
    search_queue = deque()
    search_queue += graph['A']

    while search_queue:
        letter = search_queue.popleft()
        if letter not in visited:
            if is_target_letter(letter, target):
                print("You've found {}".format(target))

                return True
            else:
                visited.append(letter)
                search_queue += graph[letter]

    return False


graph = {}
graph['A'] = ['B','C','D']
graph['B'] = ['E','F']
graph['C'] = ['E','G']
graph['D'] = []
graph['E'] = []
graph['F'] = ['H']
graph['G'] = []
graph['H'] = []

look_for_letter(graph, 'H')