def numberOfDays(day, month):
    month_list_2022 = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]

    if month == 1:
        return day - 1
    return sum(month_list_2022[: month - 1]) + day - 1


# print(numberOfDays(14, 2))
