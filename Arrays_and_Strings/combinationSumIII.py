"""

This is a backtracking question.

Find the combination.

Only numbers 1 through 9 are used.
Each number is used at most once.

Input: k = 3, n = 7
Output: [[1,2,4]]

https://leetcode.com/problems/combination-sum-iii/
"""


class Solution:
    def combinationSumOne(self, n, k):
        """
        Time Complexity: O(n!/(n-k)!)
        Space Complexity: O(k)
        """
        res = []

        def backtrack(remain, tmp, start):
            if remain < 0:
                return
            if remain == 0 and len(tmp) == k:
                res.append(tmp[:])
                return

            for i in range(start, 10):
                tmp.append(i)
                backtrack(remain - i, tmp, i + 1)
                tmp.pop()

        backtrack(n, [], 1)

        return res


if __name__ == "__main__":
    k = 3
    n = 7
    sol = Solution().combinationSumOne(n, k)
    print(sol)
