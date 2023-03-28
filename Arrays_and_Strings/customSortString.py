"""
https://leetcode.com/problems/custom-sort-string/

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

"""
from collections import Counter


class Solution:
    def solutionOne(self, s: str, order: str):
        """
        Time Complexity: O(n) Here max n value could be 26.
        Space Complexity: O(n)
        """
        cnt = Counter(s)
        # remove the elements from cnt which are seen in order string
        ans = [cnt.pop(c, 0) * c for c in order]
        # append the rest letters into ans
        for k, v in cnt.items():
            ans.append(k * v)
        return "".join(ans)


if __name__ == "__main__":
    order = "cba"
    s = "abccccd"
    print(Solution().solutionOne(s, order))
