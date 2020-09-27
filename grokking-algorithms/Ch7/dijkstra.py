graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "meta": 1
    },
    "b": {
        "a": 3,
        "meta": 5
    },
    "meta": {}
}

costs = {
    "a": 6,
    "b": 2,
    "meta": float("inf")
}

parents = {
    "a": "start",
    "b": "start",
    "meta": None
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost_index = None
    lowest_cost = float("inf")
    for index, cost in costs.items():
        if index not in processed and cost < lowest_cost:
            lowest_cost_index = index
            lowest_cost = cost

    return lowest_cost_index

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbours = graph[node]

    for n in neighbours.keys():
        new_cost = cost + neighbours[n]

        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs, parents)
