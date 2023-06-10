"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solutionOne(self, nums):
        """
        In a sorted array, always the middle element becomes root.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not nums:
            return

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.solutionOne(nums[:mid])  # copies the array everytime
        root.right = self.solutionOne(nums[mid + 1 :])

        return root

    def solutionTwo(self, nums):
        """
        Instead of copying the array, we'll use indexes

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        def _helper(low, high):
            if low < high:
                mid = low + (high - low) // 2
                return TreeNode(
                    val=nums[mid],
                    left=_helper(low, mid),
                    right=_helper(mid + 1, high),
                )

        return _helper(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution().solutionOne([-10, -3, 0, 5, 9])
    print(s)
