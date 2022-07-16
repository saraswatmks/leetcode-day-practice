"""
Pick weights randomly.
https://leetcode.com/problems/random-pick-with-weight/solution/

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

"""

import random


class Solution:
    def __init__(self, w: list):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        target = self.total_sum * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i

    def pickIndexBinarySearch(self):
        """
        Time Complexity: O(log n)
        Space Complexity: O(n)
        """

        target = self.total_sum * random.random()
        left = 0
        right = len(self.prefix_sums)
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
