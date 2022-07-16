"""
Find the max length of the chain. 
Basically, endtime and startime shouldn't overlap.

https://leetcode.com/problems/maximum-length-of-pair-chain/

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
"""


from re import L
from sys import maxsize


class Solution:
    def findLongestChainOne(self, pairs):
        """
        This is dp solution.

        Time Complexity: O(n ** 2)
        Space Complexity: O(N)
        """
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[j] + 1)

        return max(dp)

    def findLongestChainTwo(self, pairs):
        """
        Greedy solution is fastest.
        https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/225801/Proof-of-the-greedy-solution

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        # sort by end time
        N = len(pairs)
        pairs.sort(key=lambda x: x[1])

        ans = 0
        # take big neg value
        cur = -1 * maxsize

        for head, tail in pairs:
            if head > cur:
                cur = tail
                ans += 1
        return ans


if __name__ == "__main__":
    pairs = [[1, 2], [7, 8], [4, 5]]
    sol = Solution().findLongestChainTwo(pairs)
    sol = Solution().findLongestChainOne(pairs)
