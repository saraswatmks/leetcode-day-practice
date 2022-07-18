"""
Given a sorted array, find two numbers which sum to target.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
"""


class Solution:
    def twoSumOne(self, nums, target):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]

    def twoSumTwo(self, nums, target):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i
        return [-1, -1]

    def twoSumThree(self, nums, target):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            tmp = target - nums[i]
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == tmp:
                    return [i + 1, mid + 1]
                elif nums[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return [-1, -1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    sol = Solution().twoSumOne(numbers, target)
    print(sol)
