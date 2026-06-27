class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        count = 0
        update = [intervals[0]]

        for start, end in intervals[1:]:
            if start >= update[-1][1]:
                update.append([start,end])
            else:
                count += 1
                update[-1][1] = min(update[-1][1], end)

        return count