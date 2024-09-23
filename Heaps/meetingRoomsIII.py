"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

https://leetcode.com/problems/meeting-rooms-iii/description/
"""

import heapq


class Solution:
    def solutionOne(self, n, meetings):
        """
        Two heaps solution.

        TC: O(mnlogn) m meetings, n rooms
        SC: O(m + n)
        """
        booked = []  # has structure (end time, room)
        free = [*range(n)]
        res = [0] * n
        meetings.sort()

        for start, end in meetings:
            # if a booked room is free, move it to free array
            while booked and booked[0][0] <= start:
                _, room = heapq.heappop(booked)
                heapq.heappush(free, room)

            # if room is free, assign it to the meeting
            if free:
                room = heapq.heappop(free)
                heapq.heappush(booked, (end, room))
            else:
                # if no room is free, update the end time
                release, room = heapq.heappop(booked)
                heapq.heappush(booked, (release + (end - start), room))
            res[room] += 1
        return res.index(max(res))

    def solutionTwo(self, n, meetings):
        """
        TC: O(mnlogn) m meetings, n rooms
        SC: O(n)
        """
        res = [0] * n
        rooms = [(0, i) for i in range(n)]
        meetings.sort()

        for start, end in meetings:
            # if a room gets free, assign the new start in the room
            while rooms and rooms[0][0] < start:
                _, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (start, room))
            release, room = heapq.heappop(rooms)
            heapq.heappush(rooms, (release + (end - start), room))
            res[room] += 1
        return res.index(max(res))


if __name__ == "__main__":
    n = 3
    meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    sol = Solution().solutionOne(n, meetings)
    print(sol)
