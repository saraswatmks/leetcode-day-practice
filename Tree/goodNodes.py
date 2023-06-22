"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """The idea is to pass the node value to the next node using curr pointer."""

    def solutionOne(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(H) -> height of binary tree
        """
        ans = 0

        def dfs(node, curr):
            nonlocal ans
            if not node:
                return 0
            if node.val >= curr:
                curr = node.val
                ans += 1
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, root.val)
        return ans
