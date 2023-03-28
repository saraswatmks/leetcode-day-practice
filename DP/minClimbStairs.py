"""
Classic DP problem (it involves solving repeated subproblems.)

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

https://leetcode.com/problems/min-cost-climbing-stairs
"""


class Solution:
    def solutionOne(self, costs: list):
        """
        Recursive solution.
        Time Complexity: O(2^n) n-> total steps
        Space Complexity: O(n)
        """

        def dp(n):
            if n < 2:
                return costs[n]

            return costs[n] + min(dp(n - 1), dp(n - 2))

        n = len(costs)
        return min(dp(n - 1), dp(n - 2))

    def solutionTwo(self, costs: list):
        """
        Bottom up solution.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(costs)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]

    def solutionThree(self, costs: list):
        """
        Bottom up solution. Space optimised.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(costs)

        dp = dp1 = dp2 = 0  # current, previous step, previous previous step

        for i in range(2, n + 1):
            dp = min(dp1 + cost[i - 1], dp2 + cost[i - 2])
            dp2 = dp1
            dp1 = dp

        return dp1


if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().solutionThree(cost))
