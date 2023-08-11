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

        def dfs(node):
            nonlocal max_path
            if node is None:
                return 0
            # we only need 0 or positive numbers as sum, hence using max here
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            max_path = max(max_path, node.val + left + right)

            return node.val + max(left, right, 0)

        dfs(root)
        return max_path
