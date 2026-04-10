from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive = []
        set_nums = set(nums)
        for i in set_nums:
            current_consecutive = []
            current_consecutive.append(i)
            next_consecutive = i + 1
            while next_consecutive in set_nums:
                current_consecutive.append(next_consecutive)
                next_consecutive += 1

            if len(current_consecutive) > len(longest_consecutive):
                longest_consecutive = current_consecutive

        return len(longest_consecutive)    

# Example
nums = [0,3,2,5,4,6,1,1]
print(Solution().longestConsecutive(nums))  

        