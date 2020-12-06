import numpy as np
import random as rnd

# Doomsday Fuel


def solution(m):
    normalise_matrix(m)
    transient_states, absorbing_states = num_transient_and_absorbing(m)
#     get_r(m, transient_states)


# def get_r(m, transient):
#     r = []
#     for i in range(transient):
#         row = []
#         for col in range(transient, len(m[row])):
#             row.append(m[row][col])
#         r.append(row)
#     for row in r:
#         print(r)
#     return r


def num_transient_and_absorbing(m):
    transient_states = []
    absorbing_states = []

    matrix_len = len(m)
    for i, val in enumerate(m):
        if m[i][i] != 1:
            transient_states.append(i)
        else:
            absorbing_states.append(i)
    return transient_states, absorbing_states


def normalise_matrix(m):
    transient_states, absorbing_states = num_transient_and_absorbing(m)

    normalised_state_order = list(absorbing_states + transient_states)

    normalised_matrix = []
    count = 0
    for i in normalised_state_order:
        normalised_matrix.append([])
        for j in normalised_state_order:
            normalised_matrix[count].append(m[i][j])
        count += 1

    for row in m:
        print(m)
    for row in normalised_matrix:
        print(row)


print(solution([
    [0, 1, 0, 0, 1],
    [4, 0, 3, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]))
