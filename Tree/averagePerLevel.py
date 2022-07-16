"""
Calculate the average for each level of the tree.
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevelsDFS1(self, root: TreeNode):
        """
        This is a recursive DFS approach.
        Time Complexity: O(n)
        Space Complexity: O(n) if tree_is_unbalanced else O(logn)
        """
        avg = []

        def getAverage(node, depth=0):
            if node:
                if len(avg) <= depth:
                    avg.append([0, 0])
                avg[depth][0] += node.val
                avg[depth][1] += 1
                getAverage(node.left, depth + 1)
                getAverage(node.right, depth + 1)

        getAverage(root)
        return avg

    def averageOfLevelsBFS1(self, root: TreeNode):
        """
        This is a BFS approach.
        Time Complexity: O(n)
        Space Complexity: O(n) if tree_is_unbalanced else O(logn)
        """

        res = []

        q = [root]

        while q:
            total, cnt = 0, len(q)
            for _ in range(cnt):
                node = q.pop(0)
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(total * 1.0 / cnt)
        return res

    def averageOfLevelsBFS2(self, root: TreeNode):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            size = len(queue)
            s = 0
            for i in range(size):
                node = queue.pop(0)
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(s / size)
        return res
