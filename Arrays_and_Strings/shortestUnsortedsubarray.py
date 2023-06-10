"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
https://leetcode.com/problems/shortest-unsorted-continuous-subarray

Basically, find the contiguous subarray sorting which can lead to sorted entire array.

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""


class Solution:
    def solutionOne(self, nums):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        l = 0
        r = len(nums) - 1

        def findminmax(l, r):
            small = float("inf")
            big = -float("inf")

            for i in range(l, r + 1):
                small = min(small, nums[i])
                big = max(big, nums[i])

            return small, big

        # find the num from left where sorted order is broken
        while l < len(nums) and nums[l] <= nums[l + 1]:
            l += 1

        # find the num from right where sorted order is broken
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        tempmin, tempmax = findminmax(l, r + 1)

        while l > 0 and tempmin < nums[l - 1]:
            l -= 1

        while r < len(nums) and tempmax > nums[r + 1]:
            r += 1

        return r - l + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().solutionOne(nums))
