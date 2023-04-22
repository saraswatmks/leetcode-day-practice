"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

https://leetcode.com/problems/maximal-square/
"""


class Solution:
    def solutionOne(self, grid):
        """
        Recursive solution.
        Time Complexity: Exponential (Each functional call, internally makes 3 more calls.)
        Space Complexity: Stack size, exponential
        """

        def _helper(grid, i, j):
            if (
                i < 0
                or j < 0
                or i > len(grid)
                or j > len(grid[0])
                or grid[i][j] != "1"
            ):
                return 0
            left = _helper(grid, i, j - 1)
            top = _helper(grid, i - 1, j)
            corner = _helper(grid, i - 1, j - 1)
            return min(left, top, corner) + 1

        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    tmp = _helper(grid, i, j)
                    ans = max(ans, tmp)

        return ans * ans

    def solutionTwo(self, grid):
        """
        Memoization
        Time Complexity: O(m*n) m->rows, n->cols
        """

        def _helper(memo, grid, i, j):
            if i < 0 or j < 0 or i > len(grid) or j > len(grid[0]):
                memo[i][j] = 0
            if memo[i][j] != -1:
                return memo[i][j]
            left = _helper(memo, grid, i, j - 1)
            top = _helper(memo, grid, i - 1, j)
            corner = _helper(memo, grid, i - 1, j - 1)
            memo[i][j] = min(left, top, corner) + 1

            return memo[i][j]

        rows = len(grid)
        cols = len(grid[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    tmp = _helper(memo, grid, i, j)
                    ans = max(tmp, ans)

        return ans * ans


if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    # s = Solution().solutionOne(grid=grid)
    s = Solution().solutionTwo(grid=grid)
    print(s)
