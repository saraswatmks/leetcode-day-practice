"""
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

https://leetcode.com/problems/find-right-interval/description/

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
"""

import bisect


class Solution:
    def solutionOne(self, intervals):
        """
        Here we are only interested in using the start time.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        n = len(intervals)
        lst = sorted((t[0], i) for i, t in enumerate(intervals))
        res = []
        for interval in intervals:
            pos = bisect.bisect_left(lst, (interval[1],))
            if pos < n:
                res.append(lst[pos][1])
            else:
                res.append(-1)

        return res


if __name__ == "__main__":
    intervals = [[3, 4], [2, 3], [1, 2]]
    s = Solution().solutionOne(intervals)
    print(s)
