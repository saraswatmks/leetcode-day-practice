"""
Group strings into anagrams.
https://leetcode.com/problems/group-anagrams/

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]):
        """
        Time Complexity: O(k * n log n)
        Space Complexity: O(k)
        """

        dct = {}
        for word in strs:
            s = "".join(sorted(word))
            if s not in dct:
                dct[s] = [word]
            else:
                dct[s].append(word)

        return dct.values()

    def groupAnagrams2(self, strs: List[str]):
        """
        Time Complexity: O(k * N)
        Space Complexity: O(k)
        """
        dct = {}

        for word in strs:
            s = [0] * 26
            for char in word:
                s[ord(char) - ord("a")] += 1
            # we use tuple because they are immutable
            s = tuple(s)
            if s not in dct:
                dct[s] = [word]
            else:
                dct[s].append(word)

        return dct.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = Solution().groupAnagrams1(strs=strs)
    print(ans)
    strs = [""]
    ans = Solution().groupAnagrams2(strs=strs)
    print(ans)
