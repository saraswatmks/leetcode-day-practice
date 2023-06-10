"""
Check if a tree is balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of 
every node never differs by more than one.

https://leetcode.com/problems/balanced-binary-tree/description/

Input: root = [3,9,20,null,null,15,7]
Output: true
"""


class Solution:
    def solutionOne(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1
