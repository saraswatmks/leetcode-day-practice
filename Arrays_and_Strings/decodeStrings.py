"""
Given an encoded string, return its decoded string.

https://leetcode.com/problems/decode-string/description/

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""


class Solution:
    def solutionOne(self, s: str):
        """
        Time Complexity: O(M) M -> size of output answer
        Space Complexity: O(M)
        """
        # find close bracket index for the opening bracket
        closePos = {}
        st = []

        for i, c in enumerate(s):
            if c == "[":
                st.append(i)
            elif c == "]":
                # stores the closing bracket index for opening bracket
                closePos[st.pop()] = i

        def solve(l, r):
            num = 0
            ans = []

            while l <= r:
                c = s[l]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "[":
                    ans.append(num * solve(l + 1, closePos[l] - 1))
                    num = 0
                    l = closePos[l]
                else:
                    ans.append(c)
                l += 1
            return "".join(ans)

        ans = solve(0, len(s) - 1)
        return ans

    def solutionTwo(self, s: str):
        """
        Using stacks.
        Time Complexity: O(N)
        Space Complexity: O(M) M-> output length
        """
        stack = []
        curNum = 0
        curString = ""
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


if __name__ == "__main__":
    s = "3[a]2[bc2[d]]"
    print(Solution().solutionTwo(s))
