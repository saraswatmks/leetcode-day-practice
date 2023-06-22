"""
A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.

https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Idea is as follows:
    1. for a given node, we go left
    2. then we go right (until here, makes a zigzag pattern)
    3. but after step 1, we can still go left and start a new zigzag pattern onwards (left -> left -> right etc)
    3. or after step 2, we can still go right and start a new zigzag pattern onwards (right -> right -> left etc)
    """

    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node, isLeft, cnt):
            if not node:
                return cnt

            # if we come from left
            # we have two options: go right or go left but start a new path
            if isLeft:
                goright = dfs(node.right, 0, cnt + 1)  # increase the count
                stillgoleft = dfs(node.left, 1, 0)  # need to reset count
                return max(stillgoleft, goright)

            # if we come from right
            # go left or keep going right but start a new path
            goleft = dfs(node.left, 1, cnt + 1)  # increase the count
            goright = dfs(node.right, 0, 0)  # need to reset count
            return max(goleft, goright)

        return max(dfs(root.left, 1, 0), dfs(root.right, 0, 0))
