"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

https://leetcode.com/problems/partition-equal-subset-sum/description/

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""


class Solution:
    """
    This is bounded knapsack problem. Either we pick one or not.
    """

    def solutionOne(self, nums: list):
        """
        Using 2D array.
        Each cell of dp array computes the sum=s upto nums[:i].

        Time Complexity: O(len(nums) * sum(nums))
        Space Complexity: O(len(nums) * sum(nums))
        """
        s = sum(nums)
        n = len(nums)

        if s % 2 != 0:
            return False

        s //= 2

        dp = [[False] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # set only the first col as true
        for i in range(1, n + 1):
            dp[i][0] = True

        for j in range(1, s + 1):
            dp[0][j] = False

        # loop over each num
        for i in range(1, n + 1):
            # loop over each sum
            for j in range(1, s + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][s]


if __name__ == "__main__":
    nums = [1, 3, 4]
    s = Solution().solutionOne(nums)
    print(s)
