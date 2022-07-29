"""
Given an array, sort it using merge sort.
"""


class Solution:
    def mergesort(self, nums, start, end):
        """
        Find the mid, and sort each sub array.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if start > end:
            return

        mid = start + (end - start) // 2

        # left part
        self.mergesort(nums[start:mid])

        # right part
        self.mergesort(nums[mid + 1 : end])

        # merge(nums, start, end)


if __name__ == "__main__":
    nums = [2, 1, 5, 4, 6, 1]
    sol = Solution().mergesort(nums, 0, len(nums) - 1)
    print(sol)
    print(nums)
