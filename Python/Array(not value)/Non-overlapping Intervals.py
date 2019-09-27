#   O(nlogn)    O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        deleted = 0
        intervals.sort(key = lambda i:i[1])
        for i in intervals:
            if i[0] < end: #overlapp
                deleted += 1
            else: #no overlapp
                end = i[1]
        return deleted

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
'''