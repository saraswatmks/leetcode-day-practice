"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
"""


class Solution:
    def solutionOne(self, word):
        last_consonent = -1
        # we use -1 here such that
        # ans += doesn't work below until all 5 vowels indexes are filled
        # because min(seen_vw.values()) - last_consonent will give -2 otherwise, and on top doing max will always give 0
        # brilliant trick
        seen_vw = {v: -1 for v in "aeiou"}
        ans = 0

        for i, x in enumerate(word):
            if x in seen_vw:
                seen_vw[x] = i
                ans += max(min(seen_vw.values()) - last_consonent, 0)
            else:
                last_consonent = i
        return ans


if __name__ == "__main__":
    word = "cuaieuouac"
    s = Solution().solutionOne(word)
    print(s)
