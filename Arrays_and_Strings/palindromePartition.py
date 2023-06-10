"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
https://leetcode.com/problems/palindrome-partitioning/description/

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""


class Solution:
    def _isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def solutionOne(self, s: str):
        """
        Backtracking.

        Time Complexity: O(2 ^ n)
        Space Complexity: O(2 ^ n)
        """

        res = []
        # n_cnt = 0

        def dfs(s, curr):
            # nonlocal n_cnt
            if not s:
                res.append(curr)

            for i in range(1, len(s) + 1):
                print(f"checking for: {s[:i]}")
                if self._isPalindrome(s[:i]):
                    dfs(s[i:], curr + [s[:i]])
                    # n_cnt += 1

        dfs(s, [])
        return res


if __name__ == "__main__":
    s = "abcde"
    print(Solution().solutionOne(s))
