def get_maxArea(height):
    if len(height) < 1:
        return 0
    left = 0
    right = len(height) - 1
    max_value = min(height[left], height[right]) * (right - left)
    while left <= right:
        if height[left] >= height[right]:
            right -= 1
        elif height[left] < height[right]:
            left += 1
        if min(height[left], height[right]) * (right - left) > max_value:
            max_value = min(height[left], height[right]) * (right - left)
    return max_value


# test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(get_maxArea(test))
