class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        # Traverse through all elements
        for i in range(n):
            swapped = False
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    # Swap if the element is greater
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            # If no two elements were swapped, break (array is sorted)
            if not swapped:
                break
        return nums

