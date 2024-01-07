"""
Chú ý: Các kết quả được làm tròn 3 chữ số sau dấu ,
"""

import numpy as np


def get_sum_row(matrix, k):
    # Hàm này trả về tổng trên hàng thứ k của ma trận
    return round(float(np.sum(matrix[k - 1])), 3)


def get_norm2_col(matrix, k):
    # Hàm này trả về căn bậc 2 của tổng bình phương các phần tử trên cột k của ma trận matrix
    return round(
        float(np.sqrt(np.sum([item**2 for item in np.array(matrix)[:, k - 1]]))), 3
    )


def get_sum_abs_diag(matrix):
    # Hàm này trả về tổng của giá trị tuyệt đối của các phần tử trên đường chéo chính của ma trận
    return round(float(sum([abs(x) for x in np.array(matrix).diagonal()])), 3)


def get_norm2_cols(matrix):
    return [
        round(float(np.sqrt(np.sum([item**2 for item in np.array(matrix)[:, k]]))), 3)
        for k in range(np.array(matrix).shape[1])
    ]


# test = np.array([[1, 1, 1], [2, 3, 4]])
# print(get_sum_row(test, 1))
# print(get_norm2_col(test, 1))
# print(get_sum_abs_diag(test))
# print(get_norm2_cols(test))
