"""
Minimum numbers of moves required to make valid parenthesis.
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Input: s = "((("
Output: 3

"""


class Solution:
    def minAddMakeValid(self, s: str):

        ans = bal = 0
        for char in s:
            bal += 1 if char == "(" else -1
            if bal == -1:
                ans += 1
                bal = 0
        return ans + bal


if __name__ == "__main__":
    # s = "((("
    # sol = Solution().minAddMakeValid(s)
    # print(sol)
    # s = "())"
    # sol = Solution().minAddMakeValid(s)
    # print(sol)
    s = "()))(("
    sol = Solution().minAddMakeValid(s)
    print(sol)
