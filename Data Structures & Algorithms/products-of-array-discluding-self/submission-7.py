from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        products = [1] * len(nums)

        for i in range(len(nums)):
            prefix[i] *= product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        for i in range(len(nums)):
            products[i] = prefix[i] * suffix[i]
        return products