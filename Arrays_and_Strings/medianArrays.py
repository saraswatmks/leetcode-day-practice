"""
Find the median of two sorted arrays.

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

https://leetcode.com/problems/median-of-two-sorted-arrays/

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    def solutionOne(self, nums1, nums2):
        """
        TC: O(N + M)
        SC: O(1)
        """
        m = len(nums1)
        n = len(nums2)
        m1 = m2 = 0
        i = j = 0

        for _ in range((m + n) // 2 + 1):
            # m1 holds the current candidate to compute median
            # m2 holds the previous candidate to compute median
            # we need to track previous candidate for even cases (m1+m2)//2
            m2 = m1
            if i < m and j < n:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        if (n + m) % 2 == 1:
            return float(m1)
        return (m1 + m2) / 2.0


if __name__ == "__main__":
    nums1 = [1, 2, 5]
    nums2 = [4, 8, 12]
    p = Solution().solutionOne(nums1, nums2)
    print(p)
