"""
This is a sliding window question.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
"""

from collections import Counter


class Solution:
    def solutionOne(self, s: str):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        dct = Counter()
        left = 0
        res = 0
        for right, letter in enumerate(s):
            dct[letter] += 1

            while len(dct) == 3:
                # this is the trick
                res += len(s) - right
                dct[s[left]] -= 1
                if not dct[s[left]]:
                    del dct[s[left]]
                left += 1

        return res


if __name__ == "__main__":
    s = "abcabc"
    ans = Solution().solutionOne(s)
    print(ans)
