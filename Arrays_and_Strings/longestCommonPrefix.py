"""
Find the longest common prefix.
https://leetcode.com/problems/longest-common-prefix

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""

class Solution:
    def longestCommonPrefixOne(self, s):
        """
        This is using horizontal scanning. 

        Time Complexity: O(s) -> s is sum of all characters in all string
        Space Complexity: O(1)
        """
        
        if not s:
            return ""

        pref = s[0]
        
        for i in range(1, len(s)):
            # check how many chars exist in prefix
            tmp = ""
            pref_len = len(pref)
            j = 0
            while j < pref_len:
                if s[i].startswith(pref[:j]):
                    tmp = pref[:j]
                j += 1
            pref = tmp

        return pref

    def longestCommonPrefixTwo(self, s):
        """
        This is using vertical scanning. 

        Time Complexity: O(s) -> s is sum of all characters in all string
        Space Complexity: O(1)

        It is slightly better because of best time complexity.
        Worst time complexity is still the same as previous solution.
        """
        
        if not s:
            return ""
        
        for i in range(len(s[0])):
            c = s[0][i]
            for j in range(1, len(s)):
                if i == len(s[j]) or s[j][i] != c:
                    return s[0][:i]
        return s[0]

    def longestCommonPrefixThree(self, strs):
        """
        Sort the list. We just check first and last string. It works
        since sorting ensures the correct sequence of words.

        Time Complexity: O(n log n) + O(m)
        Space Complexity: O(1)
        """
        if len(strs) == 0:
            return '' 
        res = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(res+i):
                res += i
            else:
                break
        return res
    
    def longestCommonPrefixFour(self, strs) -> str:
        """
        This works because:
        lets say strs = ["corona", "correlation", "correction"] 
        then zip(*strs) = (('c', 'c', 'c'), ('o', 'o', 'o'), ('r', 'r', 'r'), ('o', 'r', 'r'), ('n', 'e', 'e'), ('a', 'l', 'c'))
        for each tuple, all chars must be same if it is shared, we stop at tuple when 
        we have more than one char.

        Time Complexity: O(S) -> S is all chars across all string.

        """
        pre=""
        for t in zip(*strs):
            if len(set(t))==1:
                pre+=t[0]
            else:
                break
        return pre


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution().longestCommonPrefixOne(strs)
    print(sol)
    strs = ["flower","flow","flight"]
    sol = Solution().longestCommonPrefixTwo(strs)
    print(sol)
