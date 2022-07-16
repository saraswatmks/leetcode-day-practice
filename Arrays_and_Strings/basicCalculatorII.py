"""
Given a string, evaluate the expression without using any inbuilt function.
https://leetcode.com/problems/basic-calculator-ii/

Input: s = "3+2*2"
Output: 7

Use BODMAS to decide the precedence given to operators.

"""


class Solution:
    def calculate(self, s: str):
        """
        Idea is to keep a pre sign

        44 / 22 * 21
        Set a default sign +
        Use previous sign when found a sign, update the sign.
        Reset the num every time a sign in encountered.

        Time Complexity: O(n)
        Space Complexity: O(n)

        """
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "-+*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)


if __name__ == "__main__":
    # s = " 3+5 / 2 "
    # sol = Solution().calculate(s)
    # print(sol)
    s = "-44/22*21"
    sol = Solution().calculate(s)
    print(sol)
