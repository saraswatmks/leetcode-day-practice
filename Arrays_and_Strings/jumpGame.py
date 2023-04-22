"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

https://leetcode.com/problems/jump-game/description/

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution:
    def solutionOne(self, nums):
        """
        Idea is to traverse from last.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        last_position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (
                i + nums[i] >= last_position
            ):  # if the number takes me to last position, make that my last position
                last_position = i

        return last_position == 0


if __name__ == "__main__":
    s = Solution().solutionOne([2, 3, 1, 1, 4])
    print(s)
