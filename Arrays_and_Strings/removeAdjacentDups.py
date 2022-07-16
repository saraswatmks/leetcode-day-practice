"""
Remove adjacent duplicates from a string.
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Input: s = "abbaca"
Output: "ca"
"""


from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str):
        """
        Time Complexity: O(n2)
        Space Complexity: O(n)
        """
        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, "")
        return s

    def removeDuplicatesTwo(self, s: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(N - D) D -> total length of all duplicates
        """
        stack = []

        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


if __name__ == "__main__":
    s = "abbaca"
    # sol = Solution().removeDuplicates(s)
    # print(sol)
    sol = Solution().removeDuplicatesTwo(s)
    print(sol)
