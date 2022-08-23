"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

https://leetcode.com/problems/meeting-rooms-ii/
"""

import heapq

class Solution:
    def minRoomsI(self, intervals):
        # sort by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        for i in intervals:
            # previous meeting  ended before the current start time, room can be reused
            if heap and heap[0] <= i[0]:
                heapq.heapreplace(heap, i[1])
            else:
                # new room is required
                heapq.heappush(heap, i[1])
        
        return len(heap)

if __name__ == "__main__":
    intr= [[0,30],[5,10],[15,20]]
    sol = Solution().minRoomsI(intr)
    print(sol)