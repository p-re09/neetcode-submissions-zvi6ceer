import re
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s != s[::-1]:
            return False
        return True

# Example
s = "tab a cat"
print(Solution().isPalindrome(s))