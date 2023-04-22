"""
Calculate the depth of the tree.
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxdepth(self, root: TreeNode):
        """
        This is a recursive DFS approach.
        Time Complexity: O(n)
        Space Complexity: O(n) if tree_is_unbalanced else O(logn)
        """
        if not root:
            return 0

        if not root.left or not root.right:
            return 1

        left_height = 1 + self.maxdepth(root.left)
        right_height = 1 + self.maxdepth(root.right)

        return max(left_height, right_height)

    def maxdepth2(self, root: TreeNode):
        """
        This is an iterative BFS approach.
        Time Complexity: O(n)
        Space Complexity: O(n) if tree_is_unbalanced else O(logn)
        """
        stack = []

        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))

        return depth

    def maxdepth3(self, root: TreeNode):
        """
        Keep increasing depth as we go down.
        Once we reach at bottom, return depth.

        Time Complexity: O(n)
        Space Complexity: O(n) if tree_is_unbalanced else O(logn)
        """

        def dfs(node, depth):
            # base case
            if not node:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            return max(left, right)

        return dfs(root, 1)
