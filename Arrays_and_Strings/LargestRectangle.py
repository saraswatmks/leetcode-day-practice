"""

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
https://leetcode.com/problems/largest-rectangle-in-histogram/

For understanding, watch: https://www.youtube.com/watch?v=lsQTYlCiU6c

Input: heights = [2,1,5,6,2,3]
Output: 10
"""


class Solution:
    def solutionOne(self, nums):
        """
        Brute Force.
        Time Complexity: O(n2)
        Space Complexity: O(1)
        """

        ans = 0
        for i in range(len(nums)):
            h = nums[i]
            for j in range(i, len(nums)):
                # track min height
                h = min(h, nums[j])
                curr_area = (j - i + 1) * h
                ans = max(ans, curr_area)

        return ans

    def solutionTwo(self, nums):
        """
        Here we keep track of index and height of the bars.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # height stack, position stack
        hstack, pstack = [], []
        maxarea = 0
        nums.append(0)  # handle the calculation for last index
        for i in range(len(nums)):
            # this is width of rectangles being tracked
            last_width = len(nums) + 1
            # height is decreasing, need to calculate area
            while len(hstack) != 0 and hstack[-1] > nums[i]:
                # last_width tracks each possible rectangle formed
                last_width = pstack[-1]
                area = (i - pstack.pop()) * hstack.pop()
                maxarea = max(maxarea, area)

            # heights are increasing, could potentially find a taller rectangle
            if len(hstack) == 0 or hstack[-1] < nums[i]:
                hstack.append(nums[i])
                # here we use last_width of the horizontal rectangle which can get formed.
                pstack.append(min(last_width, i))

        return maxarea


if __name__ == "__main__":
    nums = [2, 1, 5, 6, 2, 3]
    s = Solution().solutionOne(nums)
    s = Solution().solutionTwo(nums)
    print(s)
