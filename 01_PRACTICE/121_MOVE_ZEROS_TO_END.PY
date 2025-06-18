def moveZeroes(nums):
    index = 0  # pointer for the next non-zero position
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return nums

# Example
print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
