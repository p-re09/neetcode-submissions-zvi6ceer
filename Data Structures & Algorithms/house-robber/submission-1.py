class Solution:
    def rob(self, nums: List[int]) -> int:
        robb_1 = 0
        robb_2 = 0

        for n in nums:
            temp = max(n + robb_1, robb_2)
            robb_1 = robb_2
            robb_2 = temp

        return robb_2
