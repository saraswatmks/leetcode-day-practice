"""
https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

"""


class Solution:
    def solutionOne(self, grid):
        """
        Time Complexity: O(M x N)
        Space Complexity: O(L) -> L is max length of the island
        """

        def dfs(grid, i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return 0
            grid[i][j] = "#"
            l = dfs(grid, i, j - 1)
            r = dfs(grid, i, j + 1)
            u = dfs(grid, i - 1, j)
            d = dfs(grid, i + 1, j)
            return l + r + u + d + 1

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print("calling dfs")
                    ans = dfs(grid, i, j)
                    count = max(ans, count)

        return count


if __name__ == "__main__":

    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    sol = Solution().solutionOne(grid)
    print(sol)
