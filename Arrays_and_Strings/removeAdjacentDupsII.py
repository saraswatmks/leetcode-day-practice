"""
Remove adjacent duplicates from a string, given k.
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

"""


from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def removeDuplicatesOne(self, s: str, k: int):
        """
        This is brute force approach.

        Time Complexity: O(N2/k)
            We scan the string no more than k times.
        Space Complexity: O(N - D) D -> number of duplicates
        """
        prev_length = -1
        count = 1
        while prev_length != len(s):
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    count = 1
                if count == k:
                    s = s.replace(s[i - k + 1 : i + 1], "")
        return "".join(s)

    def removeDuplicatesTwo(self, s: str, k: int):
        """
        Here we use extra memory to improve tc.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # stack stores the char and count
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        return "".join(c * cnt for c, cnt in stack)


if __name__ == "__main__":
    s = "deeedbbcccbdaa"
    k = 3
    # sol = Solution().removeDuplicatesOne(s, k)
    # print(sol)
    sol = Solution().removeDuplicatesTwo(s, k)
    print(sol)
