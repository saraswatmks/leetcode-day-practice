"""

Given a number check minimum numbers if it can formed by summing perfect squares, then count the numbers.

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""

from collections import deque


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

        for i in range(1, int(n**0.5) + 1):
            ans = min(ans, 1 + self.numSquares(n - (i * i)))

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

            while i * i <= n:  # can write as while i <= sqrt(n)
                ans = min(ans, 1 + dfs(n - i * i, memo))
                i += 1
            memo[n] = ans
            return memo[n]

        memo = [-1] * (n + 1)
        return dfs(n, memo)

    def solutionIII(self, n: int):
        """
        This is BFS solution since we want to know the smallest path
        (lowest possible numbers which can sum to n)
        Image here: https://leetcode.com/problems/perfect-squares/solutions/71475/short-python-solution-using-bfs/?orderBy=most_votes
        """
        q = [[0, 0]]
        visited = set()
        while q:
            # s is sum, count is numbers taken or level in tree
            s, count = q.pop(0)
            count += 1
            for i in range(1, int(n**0.5) + 1):
                temp = s + i * i
                if temp > n:
                    break
                if temp in visited:
                    continue
                if temp == n:
                    return count
                if temp not in visited:
                    visited.add(temp)
                    q.append([temp, count])


if __name__ == "__main__":
    n = 15
    s = Solution().solutionIII(n)
    # print(s)
    # s = Solution().numSquaresMemo(n)
    print(s)
