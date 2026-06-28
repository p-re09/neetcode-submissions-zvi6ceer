class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        groupMax = nums[0]

        for i in range(1,len(nums)):
            currMax = max(nums[i], nums[i] + currMax)
            groupMax = max(groupMax, currMax)
        return groupMax