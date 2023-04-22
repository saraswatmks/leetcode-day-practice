"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


class Solution:
    def solutionOne(self, nums):
        """
        Idea is to send all 0s to left, 2 to right and 1s will automatically fall in between.
        """
        start = 0
        i = 0
        end = len(nums) - 1

        while i < end:
            if nums[i] == 0:
                tmp = nums[i]
                nums[i] = nums[start]
                nums[start] = tmp
                start += 1
                i += 1
            elif nums[i] == 2:
                tmp = nums[i]
                nums[i] = nums[end]
                nums[end] = tmp
                end -= 1
            else:  # nums[i] == 1
                i += 1

        return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    s = Solution().solutionOne(nums)
    print(s)
