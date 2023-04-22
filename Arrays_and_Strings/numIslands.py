"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
https://leetcode.com/problems/number-of-islands/

Logic is to find the group of unconnected 1s. 

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

"""


import queue
from collections import deque


class Solution:
    def numIslandsOne(self, grid):
        """
        This is DFS approach.

        Time Complexity: O(M X N)
        Space Complexity: O(M X N)
        """
        if not grid:
            return 0

        def dfs(grid, i, j):
            # base case
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return

            # mark visited
            grid[i][j] = "#"
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1

        return count

    def numIslandsTwo(self, grid):
        """
        This is bfs approach.

        Time Complexity: O(mxn)
        Space Complexity: O(mxn)
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    queue = [[i, j]]

                    while queue:
                        r, c = queue.pop(0)
                        for dx, dy in directions:
                            if (
                                0 <= r + dx < m
                                and 0 <= c + dy < n
                                and grid[r + dx][c + dy] == "1"
                            ):
                                queue.append([r + dx, c + dy])
                                grid[r + dx][c + dy] = "0"

        return count


if __name__ == "__main__":

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    sol = Solution().numIslandsOne(grid)
    print(sol)

    sol = Solution().numIslandsTwo(grid)
    print(sol)
