"""
Given the array, find the first missing positive number.
https://leetcode.com/problems/first-missing-positive/description/

Here, the point to remember is first missing positive number will always lie between (1, n+1)

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

"""


class Solution:
    def solutionOne(self, nums):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
        return -1

    def solutionTwo(self, nums):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
        return -1

    def solutionThree(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0

        # overwrite seen number with (n+1) + original value
        for i in range(n):
            tmp = nums[i] % (n + 1)
            if 1 <= tmp <= n:
                ind = tmp - 1
                nums[ind] += n + 1

        for i in range(n):
            if nums[i] <= n:
                return i + 1

        return n + 1


if __name__ == "__main__":
    nums = [10, 3, -1, 4, 1, 5, 6]  # [3, 4, -1, 1, 7, 9]
    s = Solution().solutionThree(nums)
    print(s)
