"""
Remove the incorrect node from the tree.
https://leetcode.com/problems/correct-a-binary-tree/

Input: root = [1,2,3], fromNode = 2, toNode = 3
Output: [1,null,3]
"""


class Solution:
    def correctBinaryTreeOne(self, root):
        """
        This is DFS approach.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        seen = set()

        def dfs(root):
            # this is invalid node
            if not root or (root.right and root.right.val in seen):
                return
            seen.add(root.val)
            root.right = dfs(root.right)
            root.left = dfs(root.left)

            return root

        return dfs(root)

    def correctBinaryTreeTwo(self, root):
        """
        This is a BFS approach.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        arr = [root]

        while arr:
            tmp = []
            seen = set()
            # go from right to left
            for node in arr:
                if node.right:
                    if node.right.right and node.right.right.val in seen:
                        node.right = None
                        return root
                    tmp.append(node.right)
                    seen.add(node.right.val)
                
                if node.left:
                    if node.left.right and node.left.right.val in seen:
                        node.left = None
                        return root
                    tmp.append(node.left)
                    seen.add(node.left.val)
                
                arr = tmp[:]
        
        return root





