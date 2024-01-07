def isPalindrome(input):
    input = str(input)
    if len(input) == 1:
        return True
    left_pivot = 0
    right_pivot = len(input) - 1
    while left_pivot < right_pivot:
        if input[left_pivot] == input[right_pivot]:
            left_pivot = left_pivot + 1
            right_pivot = right_pivot - 1
        else:
            return False
    return True

# print(isPalindrome(101301))
