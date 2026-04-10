from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Pass 2: suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output


# Example
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))  # [24,12,8,6]

        