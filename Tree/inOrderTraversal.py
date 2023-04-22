"""
Given a tree, return a list with preorder traversal output.

https://leetcode.com/problems/binary-tree-inorder-traversal/

Input: root = [1,null,2,3]
Output: [1,3,2]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalOne(self, root: TreeNode):
        """
        Recursive approach
        """
        ans = []

        def dfs(node):
            if node:
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)

        dfs(root)
        return ans

    def inorderTraversalTwo(self, root: TreeNode):
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right

        return ans
