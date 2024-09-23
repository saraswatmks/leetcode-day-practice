"""
Find plates between candles. Stars are plates, | are candles.

Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

https://leetcode.com/problems/plates-between-candles/description/
"""

import bisect


class Solution:
    def solutionOne(self, s, queries):
        """
        Time Complexity: O(N + Q log N) where N is the length of s and Q is the length of queries.
        Space Complexity: O(N)
        """
        candles = [i for i, c in enumerate(s) if c == "|"]
        ans = []

        for s, e in queries:
            l = bisect.bisect_left(candles, s)
            r = bisect.bisect_left(candles, e) - 1
            if l < r:
                ans.append(candles[r] - candles[l] - (r - l))
            else:
                ans.append(0)
        return ans

    def solutionTwo(self, s, queries):
        """
        Implementing Binary search manually.
        Time Complexity: O(N + Q log N) where N is the length of s and Q is the length of queries.
        Space Complexity: O(N)
        """
        candles = [i for i, c in enumerate(s) if c == "|"]
        ans = []

        def bns(x):
            l = 0
            r = len(candles) - 1

            while l <= r:
                mid = (l + r) // 2
                if candles[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        for s, e in queries:
            l = bns(s)
            r = bns(e + 1) - 1
            if l < r:
                ans.append(candles[r] - candles[l] - (r - l))
            else:
                ans.append(0)
        return ans

    def solutionThree(self, s, queries):
        """
        Time Complexity: O(n+m) where n is the number of queries and m is length of s
        Space Complexity: O(m)
        """
        s_len = len(s) + 1
        psum = [0] * s_len
        nxt = [float("inf")] * s_len
        prev = [0] * s_len
        res = []

        # from left to right
        for i, c in enumerate(s):
            # total sum of plates till i
            psum[i + 1] = psum[i] + (c == "|")
            # prev[i] will store the index of the last candle to the left of i
            prev[i + 1] = i if c == "|" else prev[i]

        # from right to left
        for i, c in reversed(list(enumerate(s))):
            nxt[i] = i if c == "|" else nxt[i + 1]

        for s, e in queries:
            # get indexes of candles to the left and right of s and e
            l, r = nxt[s], prev[e + 1]
            if l < r:
                res.append(r - l - (psum[r] - psum[l]))
            else:
                res.append(0)

        return res


if __name__ == "__main__":
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    print(Solution().solutionTwo(s, queries))
