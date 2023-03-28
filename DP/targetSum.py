"""
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

https://leetcode.com/problems/target-sum/description/
"""


class Solution:
    def solutionOne(self, nums: list, target: int):
        """
        Idea is to either take the positive number or negative number.

        TimeComplexity: O(m * n)
        SpaceComplexity: O(m * n)
        """
        n = len(nums)
        dic = {}

        # index is the index of array, total is the sum
        def dp(index, total):
            key = (index, total)

            if key in dic:
                return dic[key]

            if index == n:
                return int(total == target)

            dic[key] = dp(index + 1, total + nums[index]) + dp(
                index + 1, total - nums[index]
            )
            return dic[key]

        return dp(0, 0)


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(Solution().solutionOne(nums, target))
