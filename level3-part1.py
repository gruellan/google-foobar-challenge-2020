from fractions import Fraction as frac
from fractions import gcd
from functools import reduce
import numpy as np


def solution(m):
    # Edge cases

    assert len(m) == len(m[0])
    assert len(m) >= 1

    # Get variables for calculation
    m, trans, absorbing = normalise_matrix(m)

    # Another edge case
    if len(absorbing) == 1:
        return [1, 1]

    Q, R, I = get_q_r_i(m)

    # Perform calculations
    I_minus_Q = subtract(I, Q)
    F = inv(I_minus_Q)
    FR = np.matmul(F, R)

    # print(FR)
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
    cofactors = get_cofactors(m)

    # Get adjugate
    cofactors = transpose(cofactors)

    # Get adj / det
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / d
    return cofactors


def get_cofactors(m):
    # Get minors matrix
    minors = []
    for row in range(len(m)):
        new_row = []
        for col in range(len(m[0])):
            # Get sub matrix then get determinant from it
            mat = [x[:col] + x[col + 1:] for x in (m[:row] + m[row + 1:])]
            det = get_det(mat)

            # Get cofactor
            det *= (-1) ** (row + col)
            new_row.append(det)
        minors.append(new_row)

    return minors


def get_det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    for col in range(len(m)):
        sign = (-1) ** col
        cofactor = [row[: col] + row[col + 1:] for row in (m[: 0] + m[1:])]
        det += (sign * m[0][col] * get_det(cofactor))
    return det


def transpose(m):
    count = 0
    # Swap rows with cols
    for row in range(len(m)):
        for col in range(count, len(m[0])):
            m[col][row], m[row][col] = m[row][col], m[col][row]
        count += 1
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

o = [[1, 2, 3, 0, 0, 0], [4, 5, 6, 0, 0, 0], [7, 8, 9, 1, 0, 0],
     [0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

p = [[0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
     [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
     [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution(m))
print(solution(n))
print(solution(o))
print(solution(p))

m = [[0, 0, 0, 0, 3, 5, 0, 0, 0, 2], [0, 0, 4, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 4, 4, 0, 0, 0, 1, 1], [13, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 1, 8, 7, 0, 0, 0, 1, 3, 0], [1, 7, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution(m))

m = [[1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution(m))

print(solution([[0]]))