"""
Min swaps to balance a string
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

Input: s = "][]["
Output: 1
"""


class Solution:
    def minSwaps(self, s: str):
        """
        The idea is to count the number of unmatched brackets.
        Using a mathematical formula: (m + 1) / 2
        where m is no. of unmatched groups.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        seen = 0
        for ch in s:
            if ch == "[":
                seen += 1
            else:
                if seen > 0:
                    seen -= 1

        return (seen + 1) // 2

    def minSwapwithStack(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        mismatch = 0
        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    mismatch += 1
        return (mismatch + 1) // 2


if __name__ == "__main__":
    s = ["][][", "]]][[[", "[]"]
    for c in s:
        sol = Solution().minSwapwithStack(c)
        print(sol)
