from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            # 1) Build the Counter signature in O(k)
            sig = frozenset(Counter(w).items())  
            #    - Counter(w) is O(k)
            #    - .items() has at most k entries, and frozenset(...) is O(k)

            # 2) Bucket in O(1)
            groups[sig].append(w)

        return list(groups.values())

# Test
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))