"""
Given the root, check if tree is symmetric.
https://leetcode.com/problems/symmetric-tree/

A tree is symmetric if is a mirror version.

      1
    /   \
    2    2
   /\    /\
  3  4   4 3


Input: root = [1,2,2,3,4,4,3]
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val == root2.val:
            # pairs on the outer
            outPair = self.isMirror(root1.left, root2.right)
            # pairs on the inner
            inPair = self.isMirror(root1.right, root2.left)
            return outPair and inPair

        return False

    def isSymmetricOne(self, root: TreeNode):
        """
        This is recursive approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isSymmetricTwo(self, root: TreeNode):
        if root is None:
            return True

        stack = [(root.left, root.right)]

        while len(stack) > 0:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                # outer pairs
                stack.append((left.left, right.right))
                # inner pairs
                stack.append((left.right, right.left))
            else:
                return False
        return True
