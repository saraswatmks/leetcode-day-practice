"""
This is a DP problem.
Given a list of jobs, find the max profit.

https://leetcode.com/problems/maximum-profit-in-job-scheduling/

"""


from bisect import bisect_left
import heapq
from locale import currency


class Solution:
    def jobSchedulingOne(self, startTime, endTime, profit):
        """
        Using DP and Binary Search.
        Taken from: https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1430330/Python-dp-%2B-binary-search-explained

        Time Complexity: O(n * log n)
        Space Complexity: O(n)
        """
        jobs = sorted(zip(startTime, endTime, profit))
        S = [i[0] for i in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        for k in range(n - 1, -1, -1):
            temp = bisect_left(S, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[temp], dp[k + 1])

        return dp[0]

    def jobSchedulingTwo(self, startTime, endTime, profit):
        """
        This is brute force.

        Time Complexity: O(N ^ 2)
        Space Complexity: O(N)
        """
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))

        def dp(i):
            if i == n:
                return 0

            ans = dp(i + 1)  # Choice 1: Don't pick

            for j in range(i + 1, n + 1):
                # if startTime and endtime don't overlap
                if j == n or jobs[j][0] >= jobs[i][1]:
                    ans = max(ans, dp(j) + jobs[i][2])
                    break
            return ans

        return dp(0)

    def jobSchedulingThree(self, startTime, endTime, profit):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        jobs = sorted(zip(startTime, endTime, profit))
        heap = []
        curr_profit = 0
        max_profit = 0
        for start, end, profit in jobs:
            # heap[0][0] is the end time, endtime should be less than start to avoid overlap
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                curr_profit = max(curr_profit, tempProfit)

            # push the job into heap for further use
            heapq.heappush(heap, (end, curr_profit + profit))
            max_profit = max(max_profit, curr_profit + profit)

        return max_profit


if __name__ == "__main__":
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    sol = Solution().jobSchedulingOne(startTime, endTime, profit)
    print(sol)
    sol = Solution().jobSchedulingTwo(startTime, endTime, profit)
    print(sol)
    sol = Solution().jobSchedulingThree(startTime, endTime, profit)
    print(sol)
