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


def dayOfWeek(day, month):
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    first_day_2022 = day_of_week.index("Sat")
    return day_of_week[(numberOfDays(day, month) + first_day_2022) % 7]


# print(dayOfWeek(25, 12))
