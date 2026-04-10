class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        j, k = 0, len(heights) - 1

        for i in range(len(heights)):
            min_height = min(heights[j], heights[k])
            area = (k - j) * min_height

            if min_height == heights[j]:
                j += 1
            else:
                k -= 1

            res = max(res, area)

        return res