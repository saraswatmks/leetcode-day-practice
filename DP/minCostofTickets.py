"""
Find minimum cost of tickets for travel on given daays.
https://leetcode.com/problems/minimum-cost-for-tickets/

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

"""


class Solution:
    def minCostOne(self, days, costs):
        """
        Bottom Up approach.

        Time Complexity:
        Space Complexity:
        """
        travel_days = set(days)
        last_travel_day = days[-1]

        dp = [0 for _ in range(last_travel_day + 1)]

        for day in range(1, last_travel_day+1):
            if day not in travel_days:
                # if not traveling, cost until previous day
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(dp[day - 1] + costs[0],
                              dp[max(day - 7, 0)] + costs[1],
                              dp[max(day - 30, 0)] + costs[2]
                              )

        return dp[last_travel_day]

    def minCostTwo(self, days, costs):
        return


if __name__ == "__main__":
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    sol = Solution().minCostOne(days, costs)
    print(sol)
    sol = Solution().minCostTwo(days, costs)
    print(sol)
