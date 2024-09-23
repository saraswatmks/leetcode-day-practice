
"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

https://leetcode.com/problems/walls-and-gates/description/

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
from collections import deque

class Solution:
    def solutionOne(self, rooms):
        """
        BFS Solution
        Time Complexity: O(m X n)
        Space Complexity: O(m X n)
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
        
        while q:
            r, c = q.popleft()
            distance = rooms[r][c] + 1

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in dirs:
                new_x, new_y = r+dx, c+dy
                if 0 <= new_x < r_size and 0 <= new_y < c_size and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))
        return rooms
    
if __name__ == "__main__":
    sol = Solution()
    arr=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    print(sol.solutionOne(arr))
