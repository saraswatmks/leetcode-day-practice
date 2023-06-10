"""

Count the number of nodes in a tree. 
Do it faster than O(N).

https://leetcode.com/problems/count-complete-tree-nodes/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solutionOne(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(H)
        """
        cnt = 0

        def dfs(node):
            nonlocal cnt
            if not node:
                return
            cnt += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return cnt

    def solutionTwo(self, root):
        """
        Time Complexity: O(log n * log n)
        Space Complexity: O(H)
        """

        def _leftdepth(node):
            if not node:
                return 0
            return 1 + _leftdepth(node.left)

        def _rightdepth(node):
            if not node:
                return 0
            return 1 + _rightdepth(node.right)

        if not root:
            return 0

        leftdepth = _leftdepth(root.left)
        rightdepth = _rightdepth(root.right)

        if leftdepth == rightdepth:
            # in a binary tree, given a depth, num nodes = 2 ^ depth -1
            return pow(2, leftdepth) - 1
        else:
            return (
                1 + self.solutionTwo(root.left) + self.solutionTwo(root.right)
            )
