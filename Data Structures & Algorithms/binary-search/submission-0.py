class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = 0
        y = len(nums) - 1
        while x <= y:
            z = (x + y) // 2
            if nums[z] == target:
                return z
            elif nums[z] > target:
                y = z - 1
            else:
                x = z + 1

        return -1