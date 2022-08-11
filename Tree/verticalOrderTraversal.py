"""
Traverse the tree vertically.
https://leetcode.com/problems/binary-tree-vertical-order-traversal/solution/

     3
    / \
   9  20
      / \
     15  7

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

"""
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrderOne(self, root: TreeNode):
        """
        BFS with sorting.

        Time Complexity: O(n log n) -> due to sorting
        Space Complexity: O(n)
        """
        columnTable = defaultdict(list)

        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]

    def verticalOrderTwo(self, root: TreeNode):
        """
        BFS without sorting

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if root is None:
            return []

        columnTable = defaultdict(list)
        minColumn = maxColumn = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                minColumn = min(minColumn, column)
                maxColumn = max(maxColumn, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(minColumn, maxColumn + 1)]

    def verticalOrderThree(self, root: TreeNode):
        """
        DFS: Here we must keep a track of row indices as well.
        We don't need that in BFS since we iterate row wise already, so the
        sequence is automatically maintained.

        Time Complexity: O(W * H log H)
        W -> width of the binary tree
        H -> height of the tree

        Space Complexity: O(N)
        N -> number of nodes in the tree
        """
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def dfs(node, row, column):
            if node is not None:
                global min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                dfs(node.left, row + 1, column - 1)
                dfs(node.right, row + 1, column + 1)

        dfs(root, 0, 0)
        # [[get list after sorting a lst using first index, then second index] for each col, list in column table map]
        return [
            [value for x, value in sorted(lst)]
            for col, lst in sorted(columnTable.items())
        ]
