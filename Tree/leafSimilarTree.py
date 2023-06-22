"""

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

https://leetcode.com/problems/leaf-similar-trees/description

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
"""


class Solution:
    def solutionOne(self, root1, root2):
        """
        Time Complexity: O(N)
        Space Complexity: O(H) -< H is height of the tree
        """

        def dfs(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr += [node.val]

            dfs(node.left, arr)
            dfs(node.right, arr)
            return arr

        return dfs(root1, []) == dfs(root2, [])
