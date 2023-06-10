"""
This is sliding window question.

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

https://leetcode.com/problems/count-number-of-nice-subarrays/description/

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
"""


class Solution:
    def solutionOne(self, nums, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l = 0
        count = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                k -= 1
                count = 0
            while k == 0:
                k += nums[l] % 2  # if od 0 gets added, if even, 1
                l += 1
                count += 1
            res += count

        return res


if __name__ == "__main__":
    nums = [2, 8, 13, 1, 1, 2, 1, 1]
    k = 3
    s = Solution().solutionOne(nums, k)
    print(s)
