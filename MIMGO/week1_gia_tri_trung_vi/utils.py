def medianValue(input_list):
    if not input_list:
        return False
    if len(input_list) == 1:
        return float(input_list[0])
    input_list.sort()
    middle = len(input_list) / 2
    if int(middle) < middle:
        return float(input_list[int(middle)])
    else:
        return float((input_list[int(middle) - 1] + input_list[int(middle)]) / 2)


# print(medianValue([1000, 1000, 1001]))
