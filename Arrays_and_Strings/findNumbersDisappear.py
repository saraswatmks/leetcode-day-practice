"""
Find numbers not available in the array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

input: nums = [4,3,2,7,8,2,3,1]
output: [5, 6]

1. Brute force O(n2)
2. Sort & Binary Search O(nlogn)

"""

import bisect
from typing import List


class Solution:
    def findDisappearedOne(self, nums: List[int]):
        """
        This is brute force approach.
        Time Complexity: O(n2)
        Space Complexity: O(1)
        """
        return [i for i in range(1, len(nums) + 1) if i not in nums]

    def findDisappearedTwo(self, nums: List[int]):
        """
        Sort and Binary Search
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        res = []
        nums = sorted(nums)
        for i in range(1, len(nums) + 1):
            index = bisect.bisect_left(nums, i)
            if nums[index % len(nums)] != i:
                res.append(i)
        return res

    def findDisappearedThree(self, nums: List[int]):
        """
        Using hashset
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        hset = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in hset:
                res.append(i)
        return res

    def findDisappearedFour(self, nums: List[int]):
        """
        Using negation strategy
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = []

        for i in range(len(nums)):
            ix = abs(nums[i]) - 1
            if nums[ix] > 0:
                nums[ix] *= -1

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res


if __name__ == "__main__":

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    ans = Solution().findDisappearedOne(nums=nums)
    print(ans)
    ans = Solution().findDisappearedTwo(nums=nums)
    print(ans)
    ans = Solution().findDisappearedThree(nums=nums)
    print(ans)
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    ans = Solution().findDisappearedFour(nums=nums)
    print(ans)
