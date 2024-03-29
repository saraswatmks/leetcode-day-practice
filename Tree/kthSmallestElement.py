"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Input: root = [3,1,4,null,2], k = 1
Output: 1
"""


class Solution:
    def solutionOne(self, root, k):

        ans = 0

        def dfs(node):
            """Using inorder traversal"""
            nonlocal k
            if not node:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.data
                return
            dfs(node.right)

        dfs(root)
        return ans

    def solutionTwo(self, root, k):
        '''Idea is that inorder traversal returns a sorted list.'''
        res = []
        # inorder traversal returns a sorted list
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if len(res) == k:
                return 
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        # print(f'{res=}')
        return res[-1]
