"""
Chú ý: Các chỉ số bmi được làm tròn 3 chữ số sau dấu ,
"""


def get_bmi1(heights, weights):
    return [round(item[1] / (item[0] / 100) ** 2, 3) for item in zip(heights, weights)]


def get_bmi2(heights, weights, names):
    return dict(
        sorted(
            dict(
                [
                    (item[2], round(item[1] / (item[0] / 100) ** 2, 3))
                    for item in zip(heights, weights, names)
                ]
            ).items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )


def get_bmi3(heights, weights, names, thresh_hold):
    return dict(
        sorted(
            dict(
                [
                    item
                    for item in get_bmi2(heights, weights, names).items()
                    if item[1] > thresh_hold
                ]
            ).items(),
            key=lambda item: item[1],
        )
    )


# # Generating a list of 5 height values in centimeters
# heights = [170, 160, 175, 165, 180]

# # Generating a list of 5 weight values in kilograms
# weights = [70, 55, 80, 62, 90]

# names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# print(get_bmi1(heights, weights))

# print(get_bmi2(heights, weights, names))

# print(get_bmi3(heights, weights, names, 25))
