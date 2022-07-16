"""
Find the path in the tree that returns max sum.
The path should be connected i.e. should have common path. 

Idea is to see, if adding a node makes sense. 
Ignore the nodes with negative values.

https://leetcode.com/problems/binary-tree-maximum-path-sum/

Solution: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode):
        """
        Time Complexity: O(n)
        n -> number of nodes

        Space Complexity: O(d)
        d -> depth of tree
        """
        max_path = float("-inf")

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            gain_on_left = max(gain_on_left(node.left), 0)
            gain_on_right = max(gain_on_right(node.right), 0)

            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(current_max_path, max_path)

            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)
        return max_path
