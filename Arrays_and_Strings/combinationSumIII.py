"""

This is a backtracking question.

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.n

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

https://leetcode.com/problems/combination-sum-iii/
"""


class Solution:
    def combinationSumOne(self, n, k):
        """
        * Time complexity = InternalNodes in the RecursionTree   +   K * LeafNodes in RecursionTree
        *                 = (C(9,0) + C(9,1) + ... + C(9,K-1))   +   K * C(9,K)
        * In our solution, the worst case will happen when k = 8.
           Then Total Time Complexity = O(574) which is O(1) or O(nCk)
        * Space Complexity = O(k) -> Depth of Recursion tree + Size of TempList
        """

        ans = []

        def dfs(start, k, target, curr):
            if k == 0 and target == 0:
                ans.append(curr[:])
                return

            if k == 0 or target <= 0:
                return

            for i in range(start, n + 1):
                dfs(start + 1, k - 1, target - i, curr + [i])

        dfs(1, k, n, [])
        return ans


if __name__ == "__main__":
    k = 3
    n = 9
    sol = Solution().combinationSumOne(n, k)
    print(sol)
