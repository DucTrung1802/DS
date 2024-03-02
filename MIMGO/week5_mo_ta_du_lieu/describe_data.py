import scipy
import numpy as np


def get_min(x):
    # Trả về giá trị nhỏ nhất của x
    return np.round(np.min(x), 10)


def get_max(x):
    # trả về giá trị lớn nhất của x
    return np.round(np.max(x), 10)


def get_mean(x):
    # Trả về giá trị trung bình của x
    return np.round(np.mean(x), 10)


def get_std(x):
    # Trả về độ lệch chuẩn của x
    return np.round(scipy.stats.tstd(x), 10)


matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(get_min(matrix))
# print(get_max(matrix))
# print(get_mean(matrix))
# print(get_std(matrix))
