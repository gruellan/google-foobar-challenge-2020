# Input: solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
# Output: [1, 2]
#
# Input: solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
# Output: [0, 1]

def solution(graph, time_limit):
    v = len(graph)
    distances = [float("Inf")] * v
    distances[0] = 0

    # Relax edges
    for i in range(v - 1):
        break
    # Identify negative cycles
    for i in graph:
        break

    print(distances)

    print(distances)


solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0],
], 1)
