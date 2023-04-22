"""
Given an integer array nums, find a contiguous subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note: question is similar to calculate product except the self number in a list.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


class Solution:
    def solutionOne(self, nums):
        """
        This solution is a modification of kadane's algorithm.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ans = prev_min = prev_max = nums[0]

        for num in nums[1:]:
            curr_min = min(num, num * prev_min, num * prev_max)
            curr_max = max(num, num * prev_min, num * prev_max)
            ans = max(ans, curr_max)
            prev_min = curr_min
            prev_max = curr_max

        return ans

    def solutionTwo(self, nums):
        """
        Ideally is two scan twice, forward and backward to find contiguous max product.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        ans = 0
        prod = 1
        # forward pass
        for num in nums:
            prod = prod * num
            ans = max(prod, ans)
            if prod == 0:
                prod = 1

        prod = 1
        # backward pass
        for i in range(len(nums) - 1, -1, -1):
            prod = prod * nums[i]
            ans = max(ans, prod)
            if prod == 0:
                prod = 1

        return ans


if __name__ == "__main__":
    nums = [2, 3, -4, -8, -10]
    s = Solution().solutionTwo(nums)
    print(s)
    s = Solution().solutionOne(nums)
    print(s)
