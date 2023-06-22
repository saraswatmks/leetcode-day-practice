"""
Sliding Window Problem.

Flip the digits so each number in the string occurs alternatively

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
"""


class Solution:
    def solutionOne(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(2n) ~ O(n)
        """

        n = len(s)
        # no need to duplicate if string is even length
        s = s if n % 2 == 0 else s + s

        # there can be two possible answers of alternate digit strings
        ans1 = ""
        ans2 = ""

        for i in range(len(s)):
            ans1 += "1" if i % 2 == 0 else "0"
            ans2 += "0" if i % 2 == 0 else "1"

        diff1 = 0
        diff2 = 0
        res = len(s)

        l = 0

        for r in range(len(s)):
            if s[r] != ans1[r]:
                diff1 += 1
            if s[r] != ans2[r]:
                diff2 += 1

            if r - l + 1 > n:
                # slide window
                if s[l] != ans1[l]:
                    diff1 -= 1
                if s[l] != ans2[l]:
                    diff2 -= 1
                l += 1

            if r - l + 1 == n:
                res = min(res, diff1, diff2)

        return res


if __name__ == "__main__":
    # s = "111000"
    s = "10111"
    print(Solution().solutionOne(s))
