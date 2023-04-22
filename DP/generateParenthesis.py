"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution:
    def solutionOne(self, n: int):
        """
        Time Complexity: O(2^n) or n catalan number
        Space Complexity: nth Catalan Number
        """
        res = []

        def dfs(left, right, curr):
            # here think of left, right as stack for left->(, right->)
            # valid ans is found when they are equal
            if left < 0 or right < 0 or left > right:
                return
            if left == 0 and right == 0:
                res.append(curr)
                return
            dfs(left - 1, right, curr + "(")
            dfs(left, right - 1, curr + ")")

        dfs(n, n, "")
        return res


if __name__ == "__main__":
    s = Solution().solutionOne(3)
    print(s)
