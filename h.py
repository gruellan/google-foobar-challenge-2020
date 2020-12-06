from fractions import Fraction as frac
from fractions import gcd
from functools import reduce


def solution(m):
    # Your code here
    assert len(m) >= 1
    assert len(m) == len(m[0])

    probabilify_matrix(m)

    terminal_states = []
    non_terminal_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            temp = row
            terminal_states.append(row)
        else:
            non_terminal_states.append(row)

    if len(terminal_states) == 1:
        return [1, 1]

    Q = get_Q(m)
    R = get_R(m)
    I_minus_Q = subtract_matrices(get_I(Q), Q)
    F = inverse_matrix(I_minus_Q)
    FR = multiply_matrices(F, R)
    for r in FR:
        print(r)
    print("\n")
    for r in I_minus_Q:
        print(r)
    print("\n")
    
    # for r in FR:
    #     print(r)
    prob_of_terminal_states = FR[0]
    # print(prob_of_terminal_states)
    common_denominator = 1 / reduce(gcd, prob_of_terminal_states)

    result = []
    for val in prob_of_terminal_states:
        factor = common_denominator / val.denominator
        numerator = val.numerator * factor
        result.append(int(numerator))
    result.append(int(common_denominator))

    return result

# turn matrix values to probabiltiy
def probabilify_matrix(m):
    for row in m:
        denominator = sum(row)
        if not denominator == 0:
            for i in range(len(row)):
                row[i] = frac(row[i], denominator)
        else:
            for i in range(len(row)):
                row[i] = frac(0)

# get submatrix Q
def get_Q(m):
    Q = []
    for i in range(len(m)):
        if not sum(m[i]) == 0:
            temp = []
            for j in range(len(m[i])):
                if not sum(m[j]) == 0:
                    temp.append(m[i][j])
            Q.append(temp)
    return Q

# get submatrix R
def get_R(m):
    R = []
    for i in range(len(m)):
        if not sum(m[i]) == 0:
            temp = []
            for j in range(len(m[0])):
                if sum(m[j]) == 0:
                    temp.append(m[i][j])
            R.append(temp)
    return R

# subtract to 2 matrices
def subtract_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        temp = []
        for j in range(len(m1[i])):
            sub = m1[i][j] - m2[i][j]
            temp.append(sub)
        result.append(temp)
    return result


# get the identity matrix with row*col of matrix m
def get_I(m):
    I = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            if j == i:
                temp.append(frac(1))
            else:
                temp.append(frac(0))
        I.append(temp)
    return I

# multiply matrices
def multiply_matrices(m1, m2):
    product = []
    m2_cols = rotate_matrix(m2)
    for x in range(len(m1)):
        temp = []
        for y in range(len(m2_cols)):
            dot_prod = dot_product(m1[x], m2_cols[y])
            temp.append(dot_prod)
        product.append(temp)
    return product

# rotate matrix by 90*
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


'''
Here we go.
Inverse matrix m.
m is a square matrix
'''
def inverse_matrix(m):
    assert len(m) == len(m[0])

    # base case 2x2 matrix
    if len(m) == 2:
        coef = frac(1, det(m))
        inversed_matrix = [[coef * m[1][1], (-1) * coef * m[0][1]],
                           [coef * (-1) * m[1][0], coef * m[0][0]]]
        return inversed_matrix

    matrix_of_minors = get_matrix_of_minors(m)
    matrix_of_cofactors = get_matrix_of_cofactors(matrix_of_minors)
    adjugated_matrix = adjugate_matrix(matrix_of_cofactors)

    det_m = det(m)
    inversed_matrix = multiply_matrix_by_scalar(adjugated_matrix, frac(1, det_m))

    return inversed_matrix

# multiply matrix by scalar. * note that scalar is a Python Fraction
def multiply_matrix_by_scalar(m, frac_num):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = frac(m[i][j]) * frac_num
    return m

# get adjoint matrix
def adjugate_matrix(m):
    x = 0
    for i in range(len(m)):
        for j in range(x, len(m[0])):
            m[i][j], m[j][i] = m[j][i], m[i][j]
        x += 1
    return m

# get matrix of cofactors
def get_matrix_of_cofactors(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] *= (-1)**(i+j)
    return m

# get the matrix of minors of matrix
def get_matrix_of_minors(m):
    matrix_of_minors = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m[0])):
            temp.append(det(get_submatrix(m, i, j)))
        matrix_of_minors.append(temp)
    return matrix_of_minors

# find the determinate of a matrix
def det(m):
    # base case 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    det_val = 0
    for j in range(len(m[0])):
        temp = m[0][j] * det(get_submatrix(m, 0, j))
        det_val += ((-1)**j)*temp
    return det_val

# get submatrix with a given row and column
def get_submatrix(m, r, c):
    sub_m = []
    for row in (m[:r] + m[r + 1:]):
        temp = row[:c] + row[c + 1:]
        sub_m.append(temp)
    return sub_m


'''
TEST
'''
def foobarExTest1():
    test_input = [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
    ]
    print(solution(test_input))
    assert solution(test_input) == [7, 6, 8, 21]

def foobarExTest2():
    test_input = [
        [0, 1, 0, 0, 0, 1], 
        [4, 0, 0, 3, 2, 0], 
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]
    ]
    print(solution(test_input))
    assert solution(test_input) == [0, 3, 2, 9, 14]


foobarExTest1()
foobarExTest2()