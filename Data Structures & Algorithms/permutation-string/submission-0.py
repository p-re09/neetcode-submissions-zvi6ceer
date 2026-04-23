class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1

        window = {}
        l = 0

        for r in range(len(s2)):
            # add right char
            window[s2[r]] = window.get(s2[r], 0) + 1

            # keep window size == len(s1)
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            # check match
            if window == seen:
                return True

        return False