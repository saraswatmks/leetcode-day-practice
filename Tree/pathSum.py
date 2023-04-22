"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
    such that adding up all the values along the path equals the given sum.
https://leetcode.com/problems/path-sum/

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true # 5 + 4 + 11 + 2

"""


class Solution:
    def hasPathSumOne(self, root, targetSum):
        """
        BFS solution.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, curr_sum = stack.pop(0)
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))

        return False

    def hasPathSumTwo(self, root, targetSum):
        """
        This is a recursive solution.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return True

        left = self.hasPathSumTwo(root.left, targetSum)
        right = self.hasPathSumTwo(root.right, targetSum)
        return left or right
