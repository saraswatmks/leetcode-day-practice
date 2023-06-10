"""

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

https://leetcode.com/problems/jump-game-ii/description/

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution:
    def solutionOne(self, nums):
        """
        Idea is to find nums[i] such that nums[i] = i + nums[i] = last position of array

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        position = len(nums) - 1
        cnt = 0
        while position != 0:
            for i in range(0, position):
                pos_dif = position - i
                if nums[i] >= pos_dif:
                    cnt += 1
                    position = i
                    break

        return cnt

    def solutionTwo(self, nums):
        """
        This can be seen as a BFS as well. At each we can do max nums[i] steps and reach a new level.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        jumps = 0
        curEnd = 0
        curFarthest = 0
        for i in range(0, len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest

        return jumps


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    s = Solution().solutionTwo(nums)
    print(s)
