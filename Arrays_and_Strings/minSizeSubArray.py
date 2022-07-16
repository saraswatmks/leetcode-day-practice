"""
Return length which sums up to target. All nums are positive.
https://leetcode.com/problems/minimum-size-subarray-sum/

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2 # 4,3
"""


class Solution:
    def minSubArrayLenOne(self, target: int, nums: list) -> int:
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

    def minSubArrayLenTwo(self, target: int, nums: list) -> int:
        """
        This is sliding window approach.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        n = len(nums)
        INF = n + 1
        windowSum = 0
        l = 0
        ans = INF

        for r in range(n):
            windowSum += nums[r]
            while windowSum >= target:
                ans = min(ans, r - l + 1)
                windowSum -= nums[l]
                l += 1
        return ans if ans != INF else 0


if __name__ == "__main__":
    target = 4
    nums = [1, 4, 4]
    sol = Solution().minSubArrayLenOne(target, nums)
    print(sol)
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution().minSubArrayLenTwo(target, nums)
    print(sol)
