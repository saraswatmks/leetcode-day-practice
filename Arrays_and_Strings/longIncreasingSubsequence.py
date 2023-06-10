"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

https://leetcode.com/problems/longest-increasing-subsequence/
"""

import bisect


class Solution:
    def solutionOne(self, nums: list):
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        """
        n = len(nums)
        dp = [1] * (n + 1)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

        return dp

    def solutionTwo(self, nums: list):
        """
        Perform binary search on ans object.

        Time Complexity: O(n * logn)
        Space Complexty: O(n)
        """
        ans = []

        for num in nums:
            if len(ans) == 0 or ans[-1] < num:
                ans.append(num)
            else:
                # idx = bisect.bisect_left(ans, num)
                left = 0
                right = len(ans) - 1
                mid = 0
                while left <= right:
                    mid = left + (right - left) // 2
                    if ans[mid] > num:
                        right = mid - 1
                    else:
                        left = mid + 1
                ans[mid] = num

        return ans


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().solutionTwo(nums))
