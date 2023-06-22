"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

https://leetcode.com/problems/count-the-number-of-good-subarrays/description/
"""

from collections import Counter


class Solution:
    def solutionOne(self, nums, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = Counter()
        left = 0
        ans = 0
        for right in range(len(nums)):
            # this only works if the number is present in dict, otherwise subtracts 0
            k -= count[nums[right]]
            # we count every pairs
            count[nums[right]] += 1
            while k <= 0:
                # reduce the pair count
                count[nums[left]] -= 1
                # subtract k only if the left value was a part of any pair
                k = count[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    nums = [3, 1, 4, 3, 2, 2, 4]
    k = 2
    s = Solution().solutionOne(nums, k)
    print(s)
