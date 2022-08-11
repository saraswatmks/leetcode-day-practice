"""
Longest palindromic subsequence
https://leetcode.com/problems/longest-palindromic-subsequence

"""


class Solution:
    def longestPalindromeOne(self, s):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)

        """
        if s == s[::-1]:
            return len(s)

        n = len(s)
        print(f"this is {n=}")
        # we just need to store one array, so we can rewrite it in every iteration
        dp = [0 for j in range(n)]
        dp[n - 1] = 1

        # n-2 since we can compare upto two chars
        for i in range(n - 2, -1, -1):
            tmp = dp[:]
            for j in range(i + 1, n):
                print(f"Scanning through {i=}, {j=}, string: {s[i:j]}")
                if s[i] == s[j]:
                    tmp[j] = 2 + dp[j - 1]
                else:
                    tmp[j] = max(tmp[j], tmp[j - 1])
                print(f"{tmp=}")
                print("*" * 100)
            dp = tmp[:]

        return dp[n - 1]


if __name__ == "__main__":
    s = "abgxba"
    sol = Solution().longestPalindromeOne(s)
    print(sol)
