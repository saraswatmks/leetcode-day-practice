"""
Traverse through tree path and sum the numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Input: root = [1,2,3]
Output: 25 # 12 + 13
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeSumOne(root: TreeNode):
        """
        This is preorder solution or recursive dfs.

        Time Complexity: O(N) <- N is number of nodes
        Space Complexity: O(H) <- H is height of tree
        """

        def solve(node, curr_sum):
            nonlocal root_to_leaf_sum
            if node:
                curr_sum = curr_sum * 10 + node.val
                # this is leaf node
                if not node.left and not node.right:
                    root_to_leaf_sum += curr_sum

                solve(node.left, curr_sum)
                solve(node.right, curr_sum)

        root_to_leaf_sum = 0
        solve(root, 0)
        return root_to_leaf_sum

    def treeSumTwo(root: TreeNode):
        """
        This is iterative solution. Going BFS.

        Time Complexity: O(N) <- N is number of nodes
        Space Complexity: O(H) <- H is height of tree
        """

        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_num = stack.pop()
            if root:
                curr_num = curr_num * 10 + root.val
                if not root.left and not root.right:
                    root_to_leaf += curr_num
                else:
                    stack.append((root.right, curr_num))
                    stack.append((root.left, curr_num))

        return root_to_leaf

        return
