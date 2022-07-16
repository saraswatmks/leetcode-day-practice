"""
This is a sliding window problem.

Longest substring without repeating characters.
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: s = "abcabcbb"
Output: 3

"""


from collections import defaultdict


class Solution:
    def longestSubstringOne(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = ""
        maxlen = 0
        for char in s:
            if char not in res:
                res += char
            else:
                maxlen = max(maxlen, len(res))
                res = res[res.index(char) + 1 :] + char
        return maxlen

    def longestSubstringTwo(self, s: str):
        """
        This is using sliding window approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        chars = [0] * 128
        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res

    def longestSubstringThree(self, s: str):
        """
        Keep a track of seen indexes

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = defaultdict(int)
        left = 0
        output = 0
        for right in range(len(s)):
            if s[right] not in seen:
                output = max(output, right - left + 1)

            else:
                if seen[s[right]] < left:
                    output = max(output, right - left + 1)
                else:
                    left = seen[s[right]] + 1

            seen[s[right]] = right
        return output


if __name__ == "__main__":
    # s = "abcxabcbb"
    s = "tmmzuxt"
    sol = Solution().longestSubstringThree(s)
    print(sol)
