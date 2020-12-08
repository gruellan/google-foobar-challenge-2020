from fractions import Fraction as frac
from fractions import gcd
from functools import reduce
import numpy as np


def solution(m):
    # Get variables for calculation
    m, trans, absorbing = normalise_matrix(m)
    Q, R, I = get_q_r_i(m)

    # Perform calculations
    I_minus_Q = subtract(I, Q)
    F = inv(I_minus_Q)
    FR = np.matmul(F, R)

    # Find lcm
    FR = FR[0]
    lcm = int(1 / reduce(gcd, FR))

    # Convert to ints and add probabilities and lcm
    res = [int(x.numerator * lcm / x.denominator) for x in FR]
    res.append(lcm)

    return res


def normalise_matrix(m):
    trans = []
    absorbing = []
    for row in m:
        denom = sum(row)
        if denom == 0:
            absorbing.append(row)
            for i in range(len(row)):
                row[i] = frac(0)

        else:
            trans.append(row)

            # Two identical for loops to prevent div by zero error
            for i in range(len(row)):
                row[i] = frac(row[i], denom)

    return m, trans, absorbing


def get_q_r_i(m):
    Q, R, I = [], [], []

    for row in range(len(m)):
        if sum(m[row]) != 0:
            # Get Q
            new_row = []
            for col in range(len(m[row])):
                if sum(m[col]) != 0:
                    new_row.append(m[row][col])
            Q.append(new_row)

            # Get R
            new_row = []
            for col in range(len(m[0])):
                if sum(m[col]) == 0:
                    new_row.append(m[row][col])
            R.append(new_row)

    # Get I
    for row in range(len(Q)):
        new_row = []
        for col in range(len(Q)):
            new_row.append(frac(col == row))
        I.append(new_row)

    return Q, R, I


def subtract(a, b):
    rows = len(a)
    cols = len(a[0])
    res = []
    for i in range(rows):
        res.append([])
        for j in range(cols):
            res[i].append(a[i][j] - b[i][j])
    return res


def inv(m):
    d = get_det(m)

    if len(m) == 2:
        return [[m[1][1] / d, -1 * m[0][1] / d],
                [-1 * m[1][0] / d, m[0][0] / d]]

    # Get matrix of cofactors
    cofactors = []
    for row in range(len(m)):
        cofactors.append([])
        for col in range(len(m)):
            sign = (-1) ** (row + col)
            minor = get_cofactor(m, row, col)

            cofactors[row] = (sign * get_det(minor))

    # Get adjugate
    cofactors = transpose(cofactors)

    # Get adj / det
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / d
    return cofactors


def get_det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    for col in range(len(m)):
        sign = (-1) ** col
        det += (sign * m[0][col] * get_det(get_cofactor(m, 0, col)))
    return det


def get_cofactor(m, a, b):
    return [row[: b] + row[b + 1:] for row in (m[: a] + m[a + 1:])]


def transpose(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            m[col][row] = m[row][col]
    return m


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
print(solution(m))
print(solution(n))
