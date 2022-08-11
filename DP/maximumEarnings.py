"""
Find maximum earning of a taxi given a route sequence.
https://leetcode.com/problems/maximum-earnings-from-taxi/
"""

from collections import defaultdict


class Solution:
    def maxTaxiEarnings(self, n, rides):
        """
        Time Complexity: O(M + N)
            M -> length of rides
            N -> number of points
        Space Complexity: O(M + N)

        Inspired from: https://leetcode.com/problems/maximum-earnings-from-taxi/discuss/1470935/C%2B%2BPython-DP-O(M%2BN)-Clean-and-Concise
        """
        rideStartAt = defaultdict(list)
        for s, e, t in rides:
            rideStartAt[s].append([e, e - s + t])  # [end, dollar]

        dp = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            for e, d in rideStartAt[i]:
                # input can have multiple rides starting at the same point
                dp[i] = max(dp[i], dp[e] + d)
            dp[i] = max(dp[i], dp[i + 1])

        return dp[1]


if __name__ == "__main__":
    n = 20
    rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
    sol = Solution().maxTaxiEarnings(n, rides)
    print(sol)
