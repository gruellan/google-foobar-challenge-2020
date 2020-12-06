import numpy as np
import random as rnd
from functools import reduce
from fractions import Fraction, gcd
import math
# Doomsday Fuel


def solution(m):
    m, trans = normalise_matrix(m)
    absorbed = len(m) - len(trans)
    Q, R, I = get_q_r_i(m, trans, absorbed)
    i_minus_q = subtract(I, Q)
    f = np.linalg.inv(i_minus_q)
    fr = mult(f, R)

    print("R:")
    for r in R:
        print(r)
    fr = fr[0]
    for r in range(len(fr)):
        r = Fraction(r)

    lcm = abs(reduce(gcd, fr))

    res = [abs(Fraction(r/lcm)) for r in fr]
    res.append(1/lcm)

    res = [int(r) for r in res]

    print("res:")
    for r in res:
        r = abs(r)
    print(res)
    print("-------------------")


def subtract(I, Q):
    rows = len(I)
    cols = len(I[0])
    res = []
    for i in range(rows):
        res.append([])
        for j in range(cols):
            res[i].append(I[i][j]-Q[i][j])

    return res


def transpose(m):
    cols = m[0]
    rows = m
    res = []
    for c in range(len(cols)):
        res.append(m[r][c] for r in range(len(rows)))
    return res


def mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    print(C)
    return C


def rotate_matrix(m):
    cols = []
    for c in range(len(m[0])):
        temp = []
        for r in range(len(m)):
            temp.append(m[r][c])
        cols.append(temp)
    return cols


def dot_product(m1, m2):
    dot_prod = 0
    for x, y in zip(m1, m2):
        dot_prod += x * y
    return dot_prod


def get_abs(m):
    absorbing_states = []
    for i, row in enumerate(m):
        row = m[i]
        if sum(row) == 0:
            absorbing_states.append(i)

    return absorbing_states


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
    for i in range(len(Q)):
        temp = []
        for j in range(len(Q)):
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

    # for row in normalised_matrix:
    #     print(row)
    return normalised_matrix, transient_states


m = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

n = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

solution(m)
solution(n)
