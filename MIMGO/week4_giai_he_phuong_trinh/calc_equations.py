import numpy as np


def solution(A, b):
    if not len(A) and len(A[0]):
        return False
    if not len(A) and len(b):
        return False

    a_inv = np.linalg.inv(A)
    if not a_inv.shape[0]:
        return False

    x = np.linalg.solve(A, b)

    a_norm = np.linalg.norm(A)
    b_norm_square = np.square(np.linalg.norm(b))
    result = a_norm + b_norm_square
    return (np.round(a_inv, 2), np.round(x, 2), np.round(result, 2))


# A_matrix = np.array([[2, 1], [1, 1]])
# B_matrix = np.array([3, 2])
# print(solution(A_matrix, B_matrix))
