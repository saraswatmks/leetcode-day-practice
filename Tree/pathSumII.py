"""
Return the path which sums up to given targetSum.
https://leetcode.com/problems/path-sum/

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

"""


class Solution:
    def hasPathSumOne(self, root, targetSum):
        """
        This is DFS.

        Time Complexity: O(N)
        Space Complexity: O(H) <- height of the tree
        """

        def solve(node, curr_sum, tmplist):
            nonlocal res
            if node:
                curr_sum += node.val
                tmplist.append(node.val)
                if not node.left and not node.right and curr_sum == targetSum:
                    res.append(tmplist[:])
                else:
                    solve(node.left, curr_sum, tmplist)
                    solve(node.right, curr_sum, tmplist)
                # this line does backtracking.
                tmplist.pop()

        res = []
        solve(root, 0, [])

    def hasPathSumTwo(self, root, targetSum):
        """
        This is BFS.

        Time Complexity: O(N)
        Space Complexity: O(H) <- height of the tree
        """

        if not root:
            return []

        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            node, curr_sum, tmplst = queue.pop(0)
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(tmplst[:])
            if node.left:
                queue.append((node.left, curr_sum + node.left, tmplst + [node.left]))
            if node.right:
                queue.append((node.right, curr_sum + node.right, tmplst + [node.right]))
        return res
