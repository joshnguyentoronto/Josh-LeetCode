'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

class Solution(object):
    def insert(self, intervals, newInterval):
        # if intervals is empty
        if not intervals:
            return [newInterval]
        # insert newInterval into intervals
        x = len(intervals) + 1
        f = 0
        while len(intervals) != x:
            if intervals[f][0] <= newInterval[0] and f == len(intervals) - 1:
                intervals.append(newInterval)
            elif intervals[f][0] <= newInterval[0] and intervals[f+1][0] >= newInterval[0]:
                intervals.insert(f+1, newInterval)
            elif intervals[f][0] >= newInterval[0] and f == 0:
                intervals.insert(0, newInterval)
            else:
                f += 1

        # join any overlapping intervals
        i = 0
        while i < len(intervals):
            if i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [ min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1]) ]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals