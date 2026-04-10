class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store value: index
        for i, num in enumerate(nums):
            print(i)
            print(num)
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i