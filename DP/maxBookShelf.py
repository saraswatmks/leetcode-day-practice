"""
Return the maximum number of books you can take from the bookshelf.

https://leetcode.com/problems/maximum-number-of-books-you-can-take/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.
"""


class Solution:
    def solutionOne(self, books):
        """
        Monotonic stack question.
        TC: O(n)
        SC: O(n)
        """

        def ssum(x, cnt):
            cnt = min(x, cnt)
            return (x * (x + 1) - (x - cnt) * (x - cnt + 1)) // 2

        stack = []
        dp = [0] * len(books)
        ans = 0
        for i in range(len(books)):
            while stack and books[stack[-1]] > books[i] - (i - stack[-1]):
                stack.pop()
            if stack:
                dp[i] = dp[stack[-1]] + ssum(books[i], i - stack[-1])
            else:
                dp[i] = ssum(books[i], i + 1)
            ans = max(ans, dp[i])
        return ans
