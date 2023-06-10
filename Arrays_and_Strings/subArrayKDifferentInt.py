"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

https://leetcode.com/problems/subarrays-with-k-different-integers/description/

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
"""
from collections import Counter


class Solution:
    def solution_one(self, nums, k):
        """
        This question uses the following logic:

        exactly(K) = atMost(K) - atMost(K-1)

        Time Complexity: O(N) for two passes
        Space Complexity: O(k) for k elementos en el dict
        """

        def _atMost(nums, k):
            count = Counter()
            left = 0
            res = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1

            return res

        return _atMost(nums, k) - _atMost(nums, k - 1)


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2
    s = Solution().solution_one(nums, k)
    print(s)
