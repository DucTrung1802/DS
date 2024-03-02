import numpy as np


# tạo mảng 1D chứa tất cả các số nguyên chẵn từ a đến b và đổi dấu các số nằm trong đoạn từ c đến d
def even_num_opp(a, b, c, d):
    a = int(a)
    b = int(b)
    if a % 2:
        a = a + 1
    my_matrix = np.arange(a, b + 1, 2)
    my_matrix[(my_matrix >= c) & (my_matrix <= d)] *= -1
    return my_matrix


# tạo ma trận có kích thước MxN, trong đó các phần tử đường viền bằng 1, còn lại bằng 0.
def bor_array(M, N):
    my_matrix = np.zeros((M, N))
    my_matrix[0] = 1
    my_matrix[-1] = 1
    my_matrix[:, 0] = 1
    my_matrix[:, -1] = 1
    return my_matrix

# tạo ma trận cỡ MxM, trong đó 0 và 1 được đặt so le, với đường chéo chính là các số 0.
def staggered_matrix(M):
    my_matrix = np.zeros((M, M))
    my_matrix[1::2, ::2] = 1
    my_matrix[::2, 1::2] = 1
    np.fill_diagonal(my_matrix, 0)
    return my_matrix

# even_num_opp(1, 100, 20, 60)
# bor_array(6, 6)
# staggered_matrix(6)
