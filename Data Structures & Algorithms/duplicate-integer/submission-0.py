from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

mySolution = Solution()
arrayTest = [1, 2, 3, 4, 5, 6, 7, 4, 9]
print(mySolution.hasDuplicate(arrayTest))  # Output: True
