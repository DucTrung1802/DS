import numpy as np


def basic_operator_matrix(A, B):
    A = np.array(A)
    B = np.array(B)
    print(A + B)
    print(A - B)
    print(np.dot(A, B))
    print(A * 3)
    print(A.transpose())

matrix1 = np.array([[5, 2], [8, 0]])
matrix2 = np.array([[4, 2], [0, 0]])

# basic_operator_matrix(matrix1, matrix2)
