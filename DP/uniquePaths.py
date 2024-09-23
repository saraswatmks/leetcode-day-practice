"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

https://leetcode.com/problems/unique-paths/description

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution:
    def solutionOne(self, m, n):
        """
        Recursive Bottom Up
        Time Complexity: 2^(m+n)
        Space Complexity: O(m+n)
        """

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)

    def solutionTwo(self, m, n):
        """
        DP Bottom Up
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
