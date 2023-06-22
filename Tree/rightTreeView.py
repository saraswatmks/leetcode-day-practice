"""
Given the root of the tree, imagine you are standing on its right. Print all nodes on the right.

https://leetcode.com/problems/binary-tree-right-side-view/

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideViewBFSOne(self, root: TreeNode):
        """
        BFS
        Solution using two queues. Keep track of current and next level.

        Time Complexity: O(N)
        Space Complexity: O(D) D -> diameter of the tree
        """

        if root is None:
            return []

        next_level = deque([root])
        rightside = []

        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            rightside.append(node.val)

        return rightside

    def rightSideViewBFSTwo(self, root: TreeNode):

        queue = deque()
        if root:
            queue.append(root)

        res = []
        while queue:
            size, val = len(queue), 0
            for _ in range(size):
                node = queue.popleft()
                val = (
                    node.val
                )  # this was always get the right node value overwritten
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # always the value for last node per level will be pushed
            # this is not intuitive, mann must run it in a debugger to see the magic.
            res.append(val)

        return res

    def rightSideViewDFS(self, root: TreeNode):
        look_up = {}

        def dfs(node, depth):
            if not node:
                return
            # overwrites the node val from left, when right nodes are called at each level
            # here calling .left is important, otherwise wrong answers.
            look_up[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return list(look_up.values())


if __name__ == "__main__":
    pass
