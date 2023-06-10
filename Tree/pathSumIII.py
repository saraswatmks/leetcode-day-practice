"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

https://leetcode.com/problems/path-sum-iii/description/

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
"""


class Solution:
    def solutionOne(self, root, target):
        """
        We do DFS at every node.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        res = 0

        def helper(node, curr):
            nonlocal res
            if not node:
                return

            if curr + node.data == target:
                res += 1

            helper(node.left, curr + node.data)
            helper(node.right, curr + node.data)

        def dfs(node):
            if not node:
                return
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def solutionTwo(self, root, target):
        """
        We use cache.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # incase target diff at very first node = 0, we count 1 since the target is found
        cache = {0: 1}
        res = 0

        def dfs(node, curr_sum):
            nonlocal res
            if not node:
                return

            curr_sum += node.data

            res += cache.get(curr_sum - target, 0)

            cache[curr_sum] = cache.get(curr_sum, 0) + 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            # backtrack
            cache[curr_sum] = cache.get(curr_sum, 0) - 1

        dfs(root, 0)
        return res
