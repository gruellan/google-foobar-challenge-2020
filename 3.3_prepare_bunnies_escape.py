# Prepare the Bunnies' Escape
# ===========================
#
# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners,
# but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the
# escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead
# ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a
# remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately
# (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one
# wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander
# Lambda's suspicions.
#
# You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape
# pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The
# door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
#
# Write a function solution(map) that generates the length of the shortest path from the prison door to the escape
# pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number
# of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always
# passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and
# width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

#
# -- Python cases --
# Input:
# solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# Output:
#     7
#
# Input:
# solution.solution([
# [0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 0]
# ])
# Output:
#     11

# Thanks to https://codereview.stackexchange.com/a/152188

def bfs(maze, start_x, start_y):
    rows, cols = len(maze), len(maze[0])
    possible_moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    # Create maze of unvisited nodes
    distances = [[None for _ in range(rows)] for _ in range(cols)]

    # Set original distance as 1
    distances[start_x][start_y] = 1
    queue = [(start_x, start_y, 1)]

    while queue:
        x, y, dist = queue.pop(0)

        # Get all possible next moves
        all_nodes = [traverse(x, y, direction) for direction in possible_moves]

        # Find the legal next moves (inside the maze borders)
        for nx, ny in all_nodes:
            if 0 <= nx < rows and 0 <= ny < cols:
                # If previously unvisited, mark node with the distance from source
                if distances[nx][ny] is None:
                    queue.append((nx, ny, dist))
                    distances[nx][ny] = distances[x][y] + 1

    return distances


def traverse(x, y, direction):
    return x + direction[0], y + direction[1]


def solution(maze):
    rows, cols = len(maze), len(maze[0])
    start = bfs(maze, 0, 0)
    finish = bfs(maze, rows - 1, cols - 1)

    # Loop until the matrices find their midway point
    for row in range(rows):
        for col in range(cols):
            if start[row][col] and finish[row][col]:
                return min(start[row][col] + finish[row][col] - 1, float("inf"))
    return None


print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]]))

print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))
