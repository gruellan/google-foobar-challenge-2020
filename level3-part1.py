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

    # Add probabilities
    res = [int(x.numerator * lcm / x.denominator) for x in FR]

    # Add lcm
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
            for i in range(len(row)):
                row[i] = frac(row[i], denom)

    return m, trans, absorbing

def get_q_r_i(m):
    Q = R = []
    for i in range(len(m)):
        if sum(m[i]) != 0:
            row = []
            for k in range(len(m[i])):
                if sum(m[k]) != 0:
                    row.append(m[i][k])
            Q.append(row)

    R = []
    for i in range(len(m)):
        if sum(m[i]) != 0:
            row = []
            for j in range(len(m[0])):
                if sum(m[j]) == 0:
                    row.append(m[i][j])
            R.append(row)

    I = []
    for i in range(len(Q)):
        temp = []
        for j in range(len(Q)):
            if j == i:
                temp.append(frac(1))
            else:
                temp.append(frac(0))
        I.append(temp)
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

def transpose(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t 

def get_determinant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    det = 0
    for col in range(len(m)):
        sign = (-1) ** col
        det += (sign * m[0][col] * get_determinant(get_cofactor(m, 0, col)))
    return det


def get_cofactor(m, a, b):
    return [row[: b] + row[b+1:] for row in (m[: a] + m[a+1:])]


def inv(m):
    d=get_determinant(m)

    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]
    cofactors=[]
    for r in range(len(m)):
        row=[]
        for c in range(len(m)):
            minor=get_cofactor(m, r, c)
            row.append(((-1)**(r+c)) * get_determinant(minor))
        cofactors.append(row)
    cofactors=transpose(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c]=cofactors[r][c]/d
    return cofactors

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
