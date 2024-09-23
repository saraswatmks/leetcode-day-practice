"""
Find number of ways a given string could be decoded.

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

"""


class Solution:
    def solutionOne(self, s: str):
        """
        Recursion solution
        TC: O(2**n)
        SC: O(N)
        """
        if len(s) == 0 or not s:
            return 0

        def dfs(s):
            if len(s) > 0:
                if s[0] == "0":
                    return 0
            if s == "" or len(s) == 1:
                return 1
            if int(s[:2]) <= 26:
                first = dfs(s[1:])
                second = dfs(s[2:])
                return first + second
            else:
                return dfs(s[1:])

        ans = dfs(s)
        return ans

    def solutionTwo(self, s: str):
        """
        Using DP
        TC: O(n)
        SC: O(n)
        """
        if not s or s[0] == "0":
            return 0
        dp = [1] * len(s)

        for i in range(1, len(s)):
            # check first
            dp[i] = 0 if int(s[i]) == 0 else dp[i - 1]

            # check second
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2 if i > 1 else 0]

        return dp[-1]


if __name__ == "__main__":
    # ans = Solution().solutionOne("226")
    ans = Solution().solutionTwo("226")
    print(ans)
