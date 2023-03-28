"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""

# Note: this solution is heavily based on longIncreasingSubsequence.py

# TODO: Incomplete


class Solution:
    def solutionOne(self, nums: list):
        """
        Time Complexity: O(n*n)
        Space Complexity: O(n)
        """

        if not nums:
            return 0

        n = len(nums)
        m = 0
        dp = [1] * n
        cnt = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i], cnt[i] = dp[j] + 1, cnt[j]
                        # cnt[i] = cnt[j]
                        # dp[i] = dp[j] + 1
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
            m = max(m, dp[i])
        return sum(c for l, c in zip(dp, cnt) if l == m)


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    print(Solution().solutionOne(nums))
