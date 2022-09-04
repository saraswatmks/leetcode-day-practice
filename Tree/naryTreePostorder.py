"""

Do post order traversal of N ary tree.

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postOrderOne(self, root: TreeNode):
        """
        This is an iterative approach. 

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
        
        q = [root]
        ans = []

        while q:
            node = q.pop()
            if node:
                ans.append(node.val)
            for c in node.children:
                q.append(c)
        
        return ans[::-1]
    
    def postOrderTwo(self, root: TreeNode):
        res = []

        def dfs(node):
            nonlocal res
            for child in node.children:
                dfs(child)
            res.append(node.val)


        dfs(root)
        return res
            