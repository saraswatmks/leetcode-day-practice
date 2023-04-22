"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

https://leetcode.com/problems/minimum-path-sum/

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

"""


class Solution:
    def solutionOne(self, grid):
        """
        Time Complexity: O(m*n) m <- rows, n <- cols
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        # fill first row and first col
        for i in range(1, col):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]

        # fill rest of the rows, pick smallest value from diagonal
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution().solutionOne(grid)
    print(s)
