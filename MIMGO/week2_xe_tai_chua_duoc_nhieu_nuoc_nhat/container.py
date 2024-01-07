def get_maxArea(height):
    if len(height) < 1:
        return 0
    left = 0
    right = len(height) - 1
    max_value = min(height[left], height[right]) * (right - left)
    while left < right:
        if (
            height[left + 1] > height[left]
            and min(height[left + 1], height[right]) * (right - (left + 1)) > max_value
        ):
            max_value = min(height[left + 1], height[right]) * (right - (left + 1))
            left += 1
        elif (
            height[right - 1] > height[right]
            and min(height[right - 1], height[left]) * ((right - 1) - left) > max_value
        ):
            max_value = min(height[right - 1], height[left]) * ((right - 1) - left)
            right -= 1
        else:
            return max_value


# test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(get_maxArea(test))
