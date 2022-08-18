"""

This is a backtracking question.

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

        def backtrack(start, cur_list):
            ans.append(cur_list[:])

            for index in range(start, n):
                print(f"this is {index=}, {ans=}, {cur_list=}")
                print("-" * 50)
                cur_list.append(nums[index])
                backtrack(index + 1, cur_list)
                cur_list.pop()
                print(f"popped last element. {index=},{cur_list=}")

        n = len(nums)
        ans = []
        backtrack(0, [])

        return ans

    def findSubsetsThree(self, nums: List[int]):
        """
        Time Complexity: (n * 2 ^ n)
        Space Complexity: (n * 2 ^ n)
        """

        def dfs(nums, output, res):

            res.append(output[:])
            for i in range(len(nums)):
                print(f"this is {i=}, {nums=},{output=}, {res=}")
                dfs(nums[i + 1 :], output + [nums[i]], res)

        res = []
        output = []
        dfs(nums, output, res)
        return res

    def findSubsetsfour(self, nums: List[int]):
        """
        Time Complexity: (2 ^ n) or ?
        Space Complexity: (2 ^ n) or ?
        """

        def solve(nums, output, index, res):

            print(f"this is {nums=}, {output=}, {index=}, {res=}")

            # base case
            if index >= len(nums):
                res.append(output[:])
                return

            # exlucde
            print("calling exclude")
            solve(nums, output, index + 1, res)

            # include
            print("calling include")
            output.append(nums[index])
            solve(nums, output, index + 1, res)

        res = []
        output = []
        index = 0
        solve(nums, output, index, res)
        return res


if __name__ == "__main__":

    nums = [1, 2, 3]
    # ans = Solution().findSubsets(nums=nums)
    # # print(ans)
    # nums = [1, 2, 3]
    ans = Solution().findSubsetsBacktrack(nums=nums)
    # print(ans)
    # nums = [1, 2, 3]
    # ans = Solution().findSubsetsThree(nums=nums)
    # print(ans)
    # nums = [1, 2, 3]
    # ans = Solution().findSubsetsfour(nums=nums)
    # print(ans)
