def sortColors(nums):
    left = 0
    right = len(nums) - 1
    index = 0

    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    while index <= right:
        if nums[index] == 0:
            swap(left, index)
            left += 1
            index = left
            continue
        elif nums[index] == 2:
            swap(right, index)
            right -= 1
            index = left
            continue
        index += 1
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
