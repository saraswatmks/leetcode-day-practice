"""
Find longest palindrome substring.
https://leetcode.com/problems/longest-palindromic-substring/

Input: s = "babad"
Output: "bab"

"""


class Solution:
    def longestPalindrome(self, s: str):
        """
        Time complexity: O(n2) because in strings like 'aaaaaa' it will go through each string
        Space complexity: O(n2)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        longest_palindrome_start, longest_palindrome_len = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                # print(end, start, s[end], s[start])
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        return s[
            longest_palindrome_start : longest_palindrome_start
            + longest_palindrome_len
        ]

    def longestPalindrome2(self, s: str):
        """
        Time complexity: O(n2)
        Space complexity: O(1)
        """
        n = len(s)
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for i in range(0, n):
            right = i
            while right < n and s[i] == s[right]:
                right += 1

            left = i - 1
            while left > 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            palindrome_len = right - left - 1
            if palindrome_len > longest_palindrome_len:
                longest_palindrome_len = palindrome_len
                longest_palindrome_start = left + 1

        return s[
            longest_palindrome_start : longest_palindrome_start
            + longest_palindrome_len
        ]

    def longestPalindrome3(self, s: str):
        """
        Time complexity: O(n2)
        Space complexity: O(k) k -> length of longest substring
        """

        def _helper(s, l, r):
            # expand outwards
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            # idea is to start from middle and expand in both directions
            odd = _helper(s, i, i)
            even = _helper(s, i, i + 1)
            res = max(res, odd, even, key=len)

        return res


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome3(s))
