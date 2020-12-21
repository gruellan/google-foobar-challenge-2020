# Input: solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
# Output: [1, 2]
#
# Input: solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
# Output: [0, 1]
from itertools import permutations


def solution(graph, time_limit):
    v = len(graph)
    num_bunnies = v - 2
    bunny_positions = [x for x in range(1, num_bunnies + 1)]

    # Edge case
    if num_bunnies == 0:
        return []

    # Relax edges using Bellman-Ford algorithm
    distances = [[float("Inf") for _ in range(v)] for _ in range(v)]
    for i in range(v):
        for _ in range(v - 1):
            for vertex in range(v):
                for edge in range(v):
                    distances[vertex][vertex] = 0
                    distances[i][edge] = min(distances[i][vertex] + graph[vertex][edge], distances[i][edge])

    # If there's a negative cycle, all bunnies are saved
    if any([distances[i][i] < 0 for i in range(v)]):
        return bunny_positions

    # Check all path perms, starting with most bunnies saved to least saved
    # Brute force as max num of bunnies is only 5
    for bunnies_saved in range(num_bunnies, 0, -1):
        for perm in permutations(bunny_positions, bunnies_saved):
            # Work out the cost of the path
            cost = sum(distances[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))

            # Add start and end values to path
            cost += distances[0][perm[0]]
            cost += distances[perm[-1]][-1]

            # Return path that completes in the specified time
            if cost <= time_limit:
                # Sort bunny IDs as specified in the problem spec
                return [bunny - 1 for bunny in sorted(perm)]

    return distances


if __name__ == '__main__':
    print(solution([
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0],
    ], 1))
