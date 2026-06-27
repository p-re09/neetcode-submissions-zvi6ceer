class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        sum = 0
        prefix = [0] * (len(nums) + 1)
        suffix = deque([0])
        for i in range(len(nums)):
            sum += nums[i]
            prefix[i + 1] = sum
        sum = 0
        for i in range(len(nums) - 1, -1, -1):
            sum += nums[i]
            suffix.appendleft(sum)
        for i in range(len(nums) - 1, -1, -1):
            if prefix[i] == suffix[i + 1]:
                index = i

        return index
            