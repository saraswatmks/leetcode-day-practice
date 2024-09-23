"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

https://leetcode.com/problems/expression-add-operators/description/

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
"""


class Solution:
    def solutionOne(self, num, target):
        """
        TC: O(4^N)
        SC: O(N)
        """
        ans = []
        L = len(num)

        def dfs(i, total, last, expr):
            if i == L:
                if total == target:
                    ans.append(expr)
                return

            for j in range(i, L):
                n = int(num[i : j + 1])
                if i == 0:
                    dfs(j + 1, n, n, f"{n}")
                else:
                    dfs(j + 1, total + n, n, expr + f"+{n}")
                    dfs(j + 1, total - n, -n, expr + f"-{n}")
                    dfs(
                        j + 1,
                        total - last + last * n,
                        last * n,
                        expr + f"*{n}",
                    )
                if n == 0:
                    break

        dfs(0, 0, 0, "")
        return ans


if __name__ == "__main__":
    num = "232"
    target = 8
    sol = Solution().solutionOne(num, target)
    print(sol)
