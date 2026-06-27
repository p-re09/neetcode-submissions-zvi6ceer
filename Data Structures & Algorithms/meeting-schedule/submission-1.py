"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        canAttend = True
        intervals.sort(key = lambda x:x.start)
        updateEnd = intervals[0]

        for i in range(1, len(intervals)):
            if updateEnd.end > intervals[i].start:
                canAttend = False
            updateEnd = intervals[i]
        return canAttend
