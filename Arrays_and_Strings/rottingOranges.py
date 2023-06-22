"""
This is a matrix problem.

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
https://leetcode.com/problems/rotting-oranges/

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

"""

from collections import deque


class Solution:
    def rottingOrangeOne(self, grid):

        """
        Matrix problems can be solved using a graph traversal approach.

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """

        # we need to count fresh oranges as well to double check in the end if all turn rot.
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        levels = 0  # this is like depth of the graph

        while queue and fresh > 0:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if (
                        0 <= x + dx < m
                        and 0 <= y + dy < n
                        and grid[x + dx][y + dy] == 1
                    ):
                        fresh -= 1
                        grid[x + dx][y + dy] = 2
                        queue.append((x + dx, y + dy))

        # return -1 if fresh != 0 else max(levels - 1, 0)
        return levels if fresh == 0 else -1


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    sol = Solution().rottingOrangeOne(grid)
    print(sol)
