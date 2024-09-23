"""
This is a sliding window based question. Fixed window.

Given two strings s and p, return an array of all the start indices of p's anagrams in s
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]`
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

    def findAnagramsThree(self, s: str, p: str):
        """
        Using sliding window
        Time Complexity: O(N)
        Space Complexity: O(K) -> K is length of shorter string.
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        i = j = 0
        p_count = Counter(p)
        s_count = Counter()
        output = []

        while j < len(s):
            s_count[s[j]] += 1
            if j - i + 1 < np:
                j += 1
            elif j - i + 1 == np:
                # anagram length found
                if s_count == p_count:
                    output.append(i)
                # move the window and update the counter
                if s_count[s[i]] == 1:
                    del s_count[s[i]]
                else:
                    s_count[s[i]] -= 1
                i += 1
                j += 1
        return output

    def findAnagramsFour(self, s: str, p: str):
        """
        This is also sliding window.
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        i = 0
        ans = []
        p_count = Counter(p)
        for j in range(ns):

            if j - i + 1 == np:
                # get substring
                s_count = Counter(s[i : i + (j - i + 1)])
                if s_count == p_count:
                    ans.append(i)
                i += 1

        return ans


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    # sol = Solution().findAnagramsOne(s, p)
    # print(sol)
    sol = Solution().findAnagramsTwo(s, p)
    print(sol)
    sol = Solution().findAnagramsThree(s, p)
    print(sol)
    sol = Solution().findAnagramsFour(s, p)
    print(sol)
