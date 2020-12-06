import numpy as np
import random as rnd

# Doomsday Fuel


def solution(m):
    m, trans = normalise_matrix(m)
    absorbed = len(m) - len(trans)
    Q, R, I = get_q_r_i(m, trans, absorbed)
    I_arr = np.array(I)
    Q_arr = np.array(Q)
    Q_arr = np.resize(Q_arr, I_arr.shape)
    i_minus_q = np.subtract(I_arr,Q_arr)

    print("\n")
    for r in i_minus_q:
        print(r)

    print("\n")
    for r in R:
        print(r)

    print("\n")
    for r in Q:
        print(r)

    print("\n")
    for r in I:
        print(r)


def get_q_r_i(m, trans, absorbed):
    Q = []
    for row in range(len(trans)):
        q_row = []
        for col in range(len(trans)):
            q_row.append(m[row][col])
        Q.append(q_row)

    R = []
    for row in range(len(trans)):
        rRow = []
        for col in range(len(trans), len(m[row])):
            rRow.append(m[row][col])
        R.append(rRow)

    I = []
    for i in range(absorbed):
        temp = []
        for j in range(absorbed):
            if j == i:
                temp.append(1)
            else:
                temp.append(0)
        I.append(temp)
    return Q, R, I


def normalise_matrix(m):
    normalised_matrix = []
    transient_states = []
    absorbing_states = []

    for i in range(len(m)):
        row = m[i]
        new_row = []

        # Absorbing states
        if sum(row) == 0:
            absorbing_states.append(i)

            for col in row:
                new_row.append(0)

            # Add probability of turning into itself (absorbing)
            new_row[i-1] = 1

        # Transient states
        else:
            transient_states.append(i)
            for col in row:
                new_row.append(col / sum(row))

        normalised_matrix.append(new_row)

    for row in normalised_matrix:
        print(row)
    return normalised_matrix, transient_states


solution([
    [0, 1, 0, 0, 1],
    [4, 0, 3, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
])
