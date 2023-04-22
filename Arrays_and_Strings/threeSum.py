"""
Find triplets which sum up to zero.
https://leetcode.com/problems/3sum/

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


class Solution:
    def threeSum(self, nums):
        """
        The idea here is to pick one number and use twoSum approach to pick rest two numbers.

        Time Complexity: O(n log n + n2) = O(n2)
        Space Complexity: O(n)
        """
        res = []
        nums.sort()

        # -2 is done to avoid ooindex error since we need three nums
        for left in range(len(nums) - 2):
            # to avoid duplicate numbers
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, r = left + 1, len(nums) - 1
            while mid < r:
                s = nums[left] + nums[mid] + nums[r]
                if s < 0:
                    mid += 1
                elif s > 0:
                    r -= 1
                else:
                    # we found the triplets
                    res.append((nums[left], nums[mid], nums[r]))
                    # remove duplicate numbers since we have already included mid and right value in the discovered triplet
                    while mid < r and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < r and nums[r] == nums[r - 1]:
                        r -= 1
                    mid += 1
                    r -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-2, 0, 0, 2, 2]
    sol = Solution().threeSum(nums)
    print(sol)
