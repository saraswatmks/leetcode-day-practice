"""
Calculate max length of repeated subarray.

https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
"""


from collections import defaultdict
from re import L


class Solution:
    def maxLengthOne(self, nums1: list, nums2: list):
        """
        This is DP solution.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * len(n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans

    def maxLengthTwo(self, nums1: list, nums2: list):
        """
        Time Complexity: O(M * N * min(M, N))
            M, N are length of the arrays.
        Space Complexity: O(N)
        """

        bstarts = defaultdict(list)
        for i, x in enumerate(nums2):
            bstarts[x].append(i)

        maxlen = 0

        for i, x in enumerate(nums1):
            for j in bstarts[x]:
                k = 0
                while (
                    i + k < len(nums1)
                    and j + k < len(nums2)
                    and nums1[i + k] == nums2[j + k]
                ):
                    k += 1
                maxlen = max(k, maxlen)

        return maxlen


if __name__ == "__main__":
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    sol = Solution().maxLengthTwo(nums1, nums2)
    print(sol)
