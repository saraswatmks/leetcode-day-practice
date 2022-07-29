"""

Calculate power of number.

Input: num=2, power=10
Ans: 1024

"""
import functools


class Solution:
    def powerone(self, num, power):
        """
        Time Complexity: O(b)
        Space Complexity: O(b) -> since we create an array of length b.
        """
        return functools.reduce(lambda a, b: a * b, [num] * power)

    def powertwo(self, num, power):
        """
        This solution uses recursion.
        """

        # base case
        if power == 0:
            return 1

        if power == 1:
            return num

        ans = self.powertwo(num, power // 2)

        # check if num is
        if power & 1 == 0:
            return ans * ans  # 2^4 can be represented as 2^2 * 2^2
        return num * ans * ans # 2^5 can be represented as 2 * 2^2 * 2^2


if __name__ == "__main__":
    a = 2
    b = 11
    ans = Solution().powerone(a, b)
    print(ans)
    ans = Solution().powertwo(a, b)
    print(ans)
