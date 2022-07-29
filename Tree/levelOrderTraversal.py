"""
Level order traversal.
https://leetcode.com/problems/binary-tree-level-order-traversal/

     3
    / \
   9  20
      / \
     15  7
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderOne(self, root: TreeNode):
        """
        Using BFS.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            size = len(queue)
            curr = []
            for _ in range(size):
                node = queue.pop(0)
                if node:
                    curr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            res.append(curr)

        return res

    def levelOrderTwo(self, root: TreeNode):
        """
        Using BFS.
        Same as previous function, just using list index to find the level.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []

        res = [[]]
        queue = [[root, 0]]

        while queue:
            node, level = queue.pop(0)
            if len(res) <= level:
                res.append([])
            if node:
                res[level].append(node.val)
                if node.left:
                    queue.append([node.left, level + 1])
                if node.right:
                    queue.append([node.right, level + 1])

        return res
