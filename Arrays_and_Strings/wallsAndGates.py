"""

This is a matrix problem.

Given a grid, calculate the distance to the nearest gate.
https://leetcode.com/problems/walls-and-gates/

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
from collections import deque
from re import L
import sys


class Solution:
    def gateDistanceOne(self, rooms):
        """
        We iterate through all the coordinates starting from 0,0
        This is bfs approach.

        Time Complexity: O(M * N)
        Space Complexity: O(1)
        """

        if not rooms:
            return []

        r_size = len(rooms)
        c_size = len(rooms[0])

        q = deque()

        for r in range(r_size):
            for c in range(c_size):
                if rooms[r][c] == 0:
                    q.append((r, c))

        # given a coordinate, we'll move onto these coordinates
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while q:
            x, y = q.popleft()
            distance = rooms[x][y] + 1

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < r_size
                    and 0 <= new_y < c_size
                    and rooms[new_x][new_y] == 2147483647
                ):
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))

        return rooms

    def gateDistanceTwo(self, rooms):
        """
        This is dfs approach.

        Time Complexity: O(m * n)
        Space Complexity: O(1)

        """

        if not rooms:
            return []

        def dfs(rooms, r, c, distance):
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if (
                    0 <= r + x < len(rooms)
                    and 0 <= c + y < len(rooms[0])
                    and rooms[r + x][c + y] == 2147483647
                ):
                    rooms[r + x][c + y] = distance + 1
                    dfs(rooms, r + x, c + y, distance + 1)

        distance = 0
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    dfs(rooms, r, c, distance)

        return rooms


if __name__ == "__main__":
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    sol = Solution().gateDistanceOne(rooms)
    print(sol)
    sol = Solution().gateDistanceTwo(rooms)
    print(sol)
