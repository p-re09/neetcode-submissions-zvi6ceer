from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        print(Counter(s))
        print(Counter(t))

        if len(s) != len(t):
            return False

        if Counter(s) == Counter(t):
            return True
        else:
            return False