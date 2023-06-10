"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
https://leetcode.com/problems/rotting-oranges/description/

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""


class Solution:
    def solutionOne(self, grid):
        """
        Time Complexity: O(N)
        Space Complexity:  O(N)

        Follow the steps:
        1. Count the number of fresh oranges.
        2. Track the rotten oranges.
        3. Using BFS, for each rotten orange, check adjacent cells.
        """
        rows = len(grid)
        cols = len(grid[0])

        fresh_cnt = 0
        rotten = []
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "2":
                    rotten.append([i, j])
                elif grid[i][j] == "1":
                    fresh_cnt += 1

        # no fresh oranges found
        if fresh_cnt == 0:
            return -1

        while rotten and fresh_cnt:
            minutes += 1
            for _ in range(len(rotten)):
                x, y = rotten.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy

                    # check if valid values
                    if xx < 0 or xx >= rows or yy < 0 or yy >= cols:
                        continue
                    if grid[xx][yy] == "2" or grid[xx][yy] == "0":
                        continue

                    fresh_cnt -= 1
                    grid[xx][yy] = "2"

                    rotten.append([xx, yy])

        return minutes if fresh_cnt == 0 else -1


if __name__ == "__main__":
    grid = [["2", "1", "1"], ["1", "1", "0"], ["0", "1", "1"]]
    s = Solution().solutionOne(grid)
    print(s)
