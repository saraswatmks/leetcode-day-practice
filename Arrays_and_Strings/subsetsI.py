"""
Find all subsets given a array.
https://leetcode.com/problems/subsets/solution/

input: nums = [1,2,3]
output: [[], [1], [1,2], [2] ...]

"""

from typing import List


class Solution:
    def findSubsets(self, nums: List[int]):
        """
        Brute force.
        Time Complexity: O(n * 2 ^ n)
        Space Complexity: O(n * 2 ^ n)
        """
        res = [[]]
        for num in nums:
            tmp = res.copy()
            for r in tmp:
                x = r + [num]
                res.append(x)
        return res

    def findSubsetsBacktrack(self, nums: List[int]):
        """
        Time Complexity: O(n * 2 ^ n)
        Space Complexity: O(n * 2 ^ n)
        """
        ans = []

        def backtrack(start, cur_list):
            ans.append(cur_list[:])

            for index in range(start, n):
                cur_list.append(nums[index])
                backtrack(index + 1, cur_list)
                cur_list.pop()

        n = len(nums)
        backtrack(0, [])

        return ans


if __name__ == "__main__":

    nums = [1, 2, 3]
    ans = Solution().findSubsets(nums=nums)
    print(ans)
    ans = Solution().findSubsetsBacktrack(nums=nums)
    print(ans)
