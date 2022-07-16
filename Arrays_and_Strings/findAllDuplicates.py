"""
Find all duplicates in an array.
https://leetcode.com/problems/find-all-duplicates-in-an-array/

input: nums = [4,3,2,7,8,2,3,1]
output: [2, 3]

There are several approaches to this:
1. O(n2) -> traverse twice using two for loops
2. O(nlogn) -> sort the array and check the previous one
3. O(n) -> negate the seen number indexes

"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]):
        res = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res

if __name__ == "__main__":

    nums = [4,3,2,7,8,2,3,1]
    ans = Solution().findDuplicates(nums=nums)
    print(ans)
