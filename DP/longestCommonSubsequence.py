"""
Find the longest common subsequence.
https://leetcode.com/problems/longest-common-subsequence/

This is a dp problem.

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

"""
from typing import List


class Solution:
    @staticmethod
    def lcsUtil(m: int, n: int, text1: str, text2: str):

        if m == 0 or n == 0:
            return 0

        if text1[m - 1] == text2[n - 1]:
            return 1 + Solution.lcsUtil(m - 1, n - 1, text1, text2)
        else:
            return max(
                Solution.lcsUtil(m, n - 1, text1, text2),
                Solution.lcsUtil(m - 1, n, text1, text2),
            )

    def longestCommonSubsequence(self, text1, text2):
        """

        Brute force solution.

        Time Complexity: O(2 ^ n)
        Since each node will have two childs and tree will be n level deep

        Space Complexity: O(2 ^ n)
        """

        len_text1 = len(text1)
        len_text2 = len(text2)

        return self.lcsUtil(len_text1, len_text2, text1, text2)

    @staticmethod
    def lcsUtilWithdp(
        m: int, n: int, text1: str, text2: str, dp: List[List[int]]
    ):

        if m == 0 or n == 0:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]

        if text1[m - 1] == text2[n - 1]:
            dp[m][n] = 1 + Solution.lcsUtilWithdp(
                m - 1, n - 1, text1, text2, dp
            )
        else:
            dp[m][n] = max(
                Solution.lcsUtilWithdp(m, n - 1, text1, text2, dp),
                Solution.lcsUtilWithdp(m - 1, n, text1, text2, dp),
            )
        return dp[m][n]

    def longestCommonSubsequenceWithdp(self, text1, text2):
        """

        Recursive solution with memoization

        Time Complexity: O(n * m)
        n & m are the length of the strings

        Space Complexity: O(n * m)
        """

        len_text1 = len(text1)
        len_text2 = len(text2)

        # set first row and first col with 0 and rest with -1
        dp = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                dp[i][j] = -1

        return Solution.lcsUtilWithdp(len_text1, len_text2, text1, text2, dp)

    def solutionThree(self, text1, text2):
        """
        Using Bottom Up DP
        This is bottom up because we start from 1,1
        """
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(Solution().longestCommonSubsequence(text1, text2))
