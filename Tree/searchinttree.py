"""
Search a value in a binary tree
https://leetcode.com/problems/search-in-a-binary-search-tree/

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search(self, root: TreeNode, val: int):
        """
        DFS approach.
        Time Complexity: O(N) where N is number of nodes
        Space Complexity: O(N) for building recursion stack
        """
        if not root:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def iterate_search(self, root, val):
        """
        Time Complexity: O(n) <- because the question doesn't mention the tree is balanced. For
        unbalanced tree, the complexity is O(n)
        Space Complexity: O(1)
        """
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
