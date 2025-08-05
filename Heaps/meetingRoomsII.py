"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

https://leetcode.com/problems/meeting-rooms-ii/
"""

import heapq

class Solution:
    def minRoomsI(self, intervals):
        """
        TC: O(n log n)
        SC: O(n)
        """
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

    def minRoomsII(self, intervals):
        """
        Using Sweep Line technique - this is more performant since prefix sum is faster than heap push pop
        TC: O(n log n)
        SC: O(n)
        """
        timeline = defaultdict(int)

        for s, e in intervals:
            timeline[s]+=1
            timeline[e]-=1

        curr_rooms = 0
        max_rooms = 0

        for time in sorted(timeline):
            curr_rooms += timeline[time]
            max_rooms = max(max_rooms, curr_rooms)

        return max_rooms

if __name__ == "__main__":
    intr= [[0,30],[5,10],[15,20]]
    sol = Solution().minRoomsI(intr)
    print(sol)
