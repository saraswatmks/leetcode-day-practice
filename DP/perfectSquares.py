"""

Given a number check if it can formed by summing perfect squares.

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""


class Solution:
    def numSquares(self, n):
        """
        Given n, a number must be lesser than sqrt(n).
        This is DFS approach.

        To find the quick time complexity of such recursions we need
        to find the maximum depth and maximum width of the recursive
        tree. Time complexity than will be width ^ depth

        Time Complexity: O(sqrt(n) ^ n)
        Space Complexity: O(n)
        """

        if n == 0:
            return 0

        ans = n

        i = 1

        while i * i <= n:
            ans = min(ans, 1 + self.numSquares(n - (i * i)))
            i += 1

        return ans

    def numSquaresMemo(self, n):
        """
        Time Complexity: O(sqrt(n) * n)
        Space Complexity: O(n)
        """

        def dfs(n, memo):

            if n == 0:
                return 0

            if memo[n] != -1:
                return memo[n]

            ans = n

            i = 1

            while i * i <= n:
                ans = min(ans, 1 + self.numSquares(n - (i * i)))
                i += 1
            memo[n] = ans
            return memo[n]

        memo = [-1] * (n + 1)
        return dfs(n, memo)


if __name__ == "__main__":
    n = 12
    s = Solution().numSquares(n)
    print(s)
    s = Solution().numSquaresMemo(n)
    print(s)
