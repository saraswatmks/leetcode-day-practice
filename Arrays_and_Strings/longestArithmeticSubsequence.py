"""
https://leetcode.com/problems/longest-arithmetic-subsequence/
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:
    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
    A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
"""


class Solution:
    def solutionOne(self, arr):
        """
        Here idea is to store difference between numbers at each j and i.

        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        """
        dp = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # dict key is tuple
                diff = arr[j] - arr[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1

        return dp


if __name__ == "__main__":
    arr = [9, 4, 7, 2, 10]
    print(Solution().solutionOne(arr))
