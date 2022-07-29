"""
Level order traversal from bottom to top.
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

     3
    / \
   9  20
      / \
     15  7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

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
        However this is not the appropriate method of solving.
        This solution is exactly same as in levelOrderTraversal.py with reverse in the end.
        Algorithm must do a bottom up traversal.

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

        return res[::-1]

    def levelOrderTwo(self, root: TreeNode):
        """
        Bottom up traversal.

        Time Complexity:
        Space Complexity:
        """
        if not root:
            return []

        res = []
        data = []
        stack = [root]
        nCount = 1
        while stack:
            node = stack.pop(0)
            data.append(node.val)
            nCount -= 1
            if node.left:
                stack.append(root.left)
            if node.right:
                stack.append(root.right)
            if nCount == 0:
                # we append from the front to the final array.
                res = [data] + res
                data = []
                nCount = len(stack)
        return res
