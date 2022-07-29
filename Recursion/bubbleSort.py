"""
Given an array, sort it using bubble sort.
"""


class Solution:
    def bubbleSort(self, nums, n):
        """
        Compare two numbers and swap them.
        Passing n argument is a must.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        print(f"this is {nums=}")
        if n <= 1:
            return nums

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        self.bubbleSort(nums, n - 1)


if __name__ == "__main__":
    nums = [2, 1, 5, 4, 6, 1]
    sol = Solution().bubbleSort(nums, len(nums))
    print(sol)
    print(nums)
