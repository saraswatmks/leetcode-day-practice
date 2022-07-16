"""
Minimal removals to make valid parenthesis
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
"""

from re import L


class Solution:
    def minRemoveToMakeValid1(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        invalid_index = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(c)
            elif not stack:
                invalid_index.add(i)
            else:
                stack.pop()

        ans = ""
        for i, c in enumerate(s):
            if i not in invalid_index:
                ans += c

        return ans

    def minRemoveToMakeValid2(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        def _delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        s = _delete_invalid_closing(s, "(", ")")
        s = _delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]

    def minRemoveToMakeValid3(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        first_pass_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(c)

        result = []
        # count all open brackets - close brackets which are matched
        open_to_keep = open_seen - balance

        for c in first_pass_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(c)

        return "".join(result)


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    sol = Solution().minRemoveToMakeValid1(s)
    print(sol)
    s = "l(e)))et((co)d(e"
    sol = Solution().minRemoveToMakeValid2(s)
    print(sol)
    s = "l(e)))et((co)d(e"
    sol = Solution().minRemoveToMakeValid3(s)
    print(sol)
