"""
This is a sliding window based question. Fixed window.

Start index of anagrams in a string.
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
"""

from collections import Counter


class Solution:
    def findAnagramsOne(self, s: str, p: str):
        """
        Time Complexity: O(S)
        Space Complexity: O(K) -> K is length of shorter string.
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        output = []
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if p_count == s_count:
                output.append(i - np + 1)

        return output

    def findAnagramsTwo(self, s: str, p: str):
        """
        Time Complexity: O(N)
        Space Complexity: O(K) -> K is length of shorter string.
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord("a")] += 1

        output = []
        for i in range(ns):
            s_count[ord(s[i]) - ord("a")] += 1
            if i >= np:
                s_count[ord(s[i - np]) - ord("a")] -= 1
            if p_count == s_count:
                output.append(i - np + 1)

        return output


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    sol = Solution().findAnagramsOne(s, p)
    print(sol)
    sol = Solution().findAnagramsTwo(s, p)
    print(sol)
