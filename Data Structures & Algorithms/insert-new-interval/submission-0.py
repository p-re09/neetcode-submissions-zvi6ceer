class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        update = [intervals[0]]

        for start, end in intervals[1:]:
            if update[-1][1] >= start:
                update[-1][1] = max(update[-1][1], end)
            else:
                update.append([start,end])
        
        return update
