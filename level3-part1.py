import numpy as np
import random as rnd
from functools import reduce
from fractions import Fraction as frac, gcd

# Doomsday Fuel


def solution(m):
    m, trans = normalise_matrix(m)
    absorbed = len(m) - len(trans)
    Q, R, I = get_q_r_i(m, trans, absorbed)
    i_minus_q = subtract(I, Q)
    f = inverse(i_minus_q)
    fra = np.matmul(f, R)

    print(Q)
    # lcm = np.lcm.reduce([fr.denominator for fr in fra])

    # vals = [int(fr.numerator * lcm / fr.denominator) for fr in fra]
    # vals.append(lcm)
    # # print(vals)
    # lcm = abs(reduce(gcd, fra))
    
    # print(lcm)
    res = []
    # print(lcm)

    print("res:")
    for r in res:
        r = abs(r)
    # print(res)
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


def inverse(m):
    d=get_determinant(m)


    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    # find matrix of cofactors
    cofactors=[]
    for r in range(len(m)):
        cofactorRow=[]
        for c in range(len(m)):
            minor=get_cofactor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * get_determinant(minor))
        cofactors.append(cofactorRow)
    cofactors=transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c]=cofactors[r][c]/d
    return cofactors


def get_i(m):
    I=[]
    for i in range(m):
        temp=[]
        for j in range(m):
            if j == i:
                temp.append(frac(1))
            else:
                temp.append(frac(0))
        I.append(temp)
    return I


def get_abs(m):
    absorbing_states=[]
    for i, row in enumerate(m):
        row=m[i]
        if sum(row) == 0:
            absorbing_states.append(i)

    return absorbing_states


def get_q_r_i(m, trans, absorbed):
    Q=[]
    for row in range(len(trans)):
        q_row=[]
        for col in range(len(trans)):
            q_row.append(m[row][col])
        print(q_row)
        Q.append(q_row)

    R=[]
    for row in range(len(trans)):
        rRow=[]
        for col in range(len(trans), len(m[row])):
            rRow.append(m[row][col])
        R.append(rRow)
    I=get_i(len(Q))
    return Q, R, I


def normalise_matrix(m):
    normalised_matrix=[]
    transient_states=[]
    absorbing_states=[]

    for i in range(len(m)):
        row=m[i]
        new_row=[]

        # Absorbing states
        if sum(row) == 0:
            absorbing_states.append(i)

            for col in row:
                new_row.append(frac(0))

            # Add probability of turning into itself (absorbing)
            new_row[i-1]=1

        # Transient states
        else:
            denom = sum(row)
            if not denom == 0:
                for i in row:
                    new_row.append(frac(row[i], denom))
            else:
                for col in row:
                    new_row.append(frac(0))
            transient_states.append(i)

        normalised_matrix.append(new_row)

    return normalised_matrix, transient_states


m=[
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

n=[
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

solution(m)
solution(n)
