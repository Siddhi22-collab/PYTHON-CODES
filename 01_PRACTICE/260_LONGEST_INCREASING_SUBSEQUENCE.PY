from bisect import bisect_left

def lengthOfLIS(nums):
    sub = []
    for x in nums:
        if not sub or x > sub[-1]:
            sub.append(x)
        else:
            idx = bisect_left(sub, x)
            sub[idx] = x
    return len(sub)

# Example:
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))  # Output: 4
