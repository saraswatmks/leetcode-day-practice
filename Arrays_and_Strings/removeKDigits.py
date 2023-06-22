"""
This is Monotonic Stack Question.

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

https://leetcode.com/problems/remove-k-digits/description/

"""


class Solution:
    def solutionOne(self, nums, k):
        """
        Idea is to remove the greatest numbers from most significant places (on hundred, thousand places i.e. start from left)

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        stack = []

        for num in nums:
            # if prev num is greater than current
            while stack and k > 0 and stack[-1] > num:
                stack.pop()
                k -= 1

            if stack or num != "0":  # prevent leading zero
                stack.append(num)

        return "".join(stack) or "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    s = Solution().solutionOne(num, k)
    print(s)
