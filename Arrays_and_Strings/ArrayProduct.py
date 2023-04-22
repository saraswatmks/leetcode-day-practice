"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution:
    def solutionOne(self, nums):
        """
        We calculate prefix and suffix sum for a given index, excluding the number at the particular index.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [1] * len(nums)

        # left to right
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        tmp = 1
        # right to left
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            res[i] *= tmp

        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    s = Solution().solutionOne(nums)
    print(s)
