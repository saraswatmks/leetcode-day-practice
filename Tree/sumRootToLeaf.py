"""
Traverse through tree path and sum the numbers,
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Input: root = [1,2,3]
Output: 25 # 12 + 13

Input: root = [4,9,0,5,1]
Output: 1026

Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeSumOne(self, root: TreeNode):
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
