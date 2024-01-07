"""
1. Thực hiện hàm get_mean_height(family_height): Trả về chiều cao trung bình của cả gia đình.
2. Thực hiện hàm get_highest_person(family_height):  Tìm người cao nhất nhà.
3. Thực hiện hàm get_height_difference(family_height): Trả về một mảng chứa độ chênh lệch chiều cao của lần lượt: mẹ-bố, mẹ-con, bố-con.
4. Thực hiện hàm get_min_difference(family_height): Tìm độ chênh lệch chiều cao nhỏ nhất trong nhà.
Chú y: Các kết quả được làm tròn 4 chữ số sau dấu , 
"""

from itertools import combinations


def get_mean_height(family_height):
    if len(family_height) == 0:
        return False
    return round((sum(family_height.values()) / len(family_height)), 4)


def get_highest_person(family_height):
    return sorted(family_height.items(), key=lambda x: x[1], reverse=True)[0][0]


def get_height_difference(family_height):
    return [round((abs(a - b)), 4) for a, b in combinations(family_height.values(), 2)]


def get_min_difference(family_height):
    return round((min(get_height_difference(family_height))), 4)


# family_height = {"mom": 160, "dad": 170.5, "son": 175.2}
# print(get_mean_height(family_height))
# print(get_highest_person(family_height))
# print(get_height_difference(family_height))
# print(get_min_difference(family_height))
