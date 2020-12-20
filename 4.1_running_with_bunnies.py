# Input: solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
# Output: [1, 2]
#
# Input: solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
# Output: [0, 1]

def solution(graph, time_limit):
    v = len(graph)
    distances = [[float("Inf") for _ in range(v)] for _ in range(v)]

    # Relax edges
    for i in range(v):
        for _ in range(v - 1):
            for vertex in range(v):
                for edge in range(v):
                    distances[vertex][vertex] = 0
                    distances[i][edge] = min(distances[i][vertex] + graph[vertex][edge], distances[i][edge])

    # Identify negative cycles
    for i in graph:
        break

    print(distances)


solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0],
], 1)
