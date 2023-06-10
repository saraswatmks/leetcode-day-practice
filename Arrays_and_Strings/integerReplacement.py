"""
https://leetcode.com/problems/integer-replacement/
Given a positive integer n, you can apply one of the following operations:

    If n is even, replace n with n / 2.
    If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.

Also, a variation of this question was asked in Facebook.

# https://leetcode.com/discuss/interview-question/736590/Facebook-Question
The question is to find the fewest number of operations needed to get to 1.
available opperations:
- add 1
- subtract 1
- divide by 2

input: 15
output: 5
because:
15->16->8->4->2->1

"""


class Solution:
    def solutionOne(self, n):
        """
        This is recursive solution.
        Time Complexity: O(log(n))
        Space Complexity: O(n)
        """
        if n == 0:
            return 1
        if n == 1:
            return 0
        # even number
        if n % 2 == 0:
            return 1 + self.solutionOne(n // 2)
        first = 1 + self.solutionOne(n - 1)
        second = 1 + self.solutionOne(n + 1)
        return min(first, second)

    def solutionTwo(self, n):
        """
        This is memoization solution.
        Time Complexity: O(log(n))
        Space Complexity: O(log(n)) -> space is reduced, since calls are reduced
        """

        def solve(n, dp):
            if n == 0:
                return 1

            if n == 1:
                return 0

            if n in dp:
                return dp[n]

            if n % 2 == 0:
                dp[n] = 1 + solve(n // 2, dp)
            else:
                dp[n] = min(1 + solve(n - 1, dp), 1 + solve(n + 1, dp))

            return dp[n]

        dp = [-1] * (n + 2)
        return solve(n, dp)

    def solutionThree(self, n):
        """
        BFS Solution.
        Time Complexity: O(log n)
        Space Complexity: O(log(n))
        """
        q = [n]
        seen = set()
        ans = 0

        while q:
            size = len(q)
            for _ in range(size):
                tmp = q.pop(0)

                if tmp == 1:
                    return ans
                if tmp in seen:
                    continue
                seen.add(tmp)

                if tmp % 2 != 0:
                    q.append(tmp + 1)
                    q.append(tmp - 1)
                else:
                    q.append(tmp // 2)
            ans += 1

        return ans


if __name__ == "__main__":
    n = 15
    s = Solution().solutionThree(n)
    print(s)
