"""
Given an array of integers, return list of numbers which sum up to target

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

"""


class Solution:
    def combinationSumI(self, nums: list, target: int):
        """
        Time Complexity: O(k * 2 ^ target)
            k -> average length of the combinations
        Space Complexity:
        """
        ans = []

        def dfs(remain, curr, start):
            # base case
            if remain < 0:
                return
            elif remain == 0:
                ans.append(curr)
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(remain - nums[i], curr, i)
                curr.pop()

        dfs(nums, [], 0)
        return ans
