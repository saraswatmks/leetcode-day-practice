"""
Given a list of intervals, merge them.
https://leetcode.com/problems/merge-intervals/

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

from typing import List


class Solution:
    def mergeIntervalsOne(self, intervals: List[List[int]]):
        """
        Brute force approach. Doesn't work.

        Time Complexity: O(n2)
        Space Complexity: O(n2)
        """
        ans = []
        intervals.sort()
        for i in range(len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            for j in range(i + 1, len(intervals)):
                c = intervals[j][0]
                d = intervals[j][1]
                if b >= c:
                    ans.append([a, max(b, d)])
                    break
            ans.append([a, b])
        return ans

    def mergeIntervalsTwo(self, intervals: List[List[int]]):
        """
        Using sorting and single pass.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        intervals.sort()
        merged = []

        for i in intervals:
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # sol = Solution().mergeIntervalsOne(intervals)
    # print(sol)
    sol = Solution().mergeIntervalsTwo(intervals)
    print(sol)
