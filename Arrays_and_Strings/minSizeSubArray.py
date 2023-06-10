"""
Return length which sums up to target. All nums are positive.
https://leetcode.com/problems/minimum-size-subarray-sum/

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2 # 4,3
"""


class Solution:
    def solutionOne(self, target: int, nums: list) -> int:
        """
        This is brute force approach.

        Time Complexity: O(n ** 2)
        Space Complexity: O(1)
        """
        min_len = float("inf")

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(min_len, j - i + 1)
        return min_len

    def solutionTwo(self, target: int, nums: list) -> int:
        """
        This is sliding window approach.
        This is O(N) because the inner while loop is independent of outer for loop

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        l = r = 0
        curr = 0
        res = len(nums)

        while r < len(nums):
            curr += nums[r]

            while curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            r += 1

        return res


if __name__ == "__main__":
    target = 4
    nums = [1, 4, 4]
    sol = Solution().solutionOne(target, nums)
    print(sol)
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution().solutionTwo(target, nums)
    print(sol)
