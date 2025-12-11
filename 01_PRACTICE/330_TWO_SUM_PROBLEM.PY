def two_sum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in mp:
            return mp[rem], i
        mp[num] = i

print(two_sum([2,7,11,15], 9))
