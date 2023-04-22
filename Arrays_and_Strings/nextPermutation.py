"""
Basically the idea is to find the next bigger number than the given in the list. If does not exist, return None.
To solve this question, you must know the technique as shown below.

https://leetcode.com/problems/next-permutation/description/

Input: nums = [1,2,3]
Output: [1,3,2]
"""


class Solution:
    def solutionOne(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = j = len(nums) - 1
        # first we find the max number from strictly decreasing sub sequence
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # means the given list is already in decreasing order, answer doesn't exist
        if i == 0:
            nums.reverse()
            return

        # this is one number before max number, this is pivot
        k = i - 1

        # find the number to swap with the pivot number
        while nums[j] <= nums[k]:
            j -= 1

        # now swap
        nums[k], nums[j] = nums[j], nums[k]

        # now reverse the rest of the array
        l = k + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums


if __name__ == "__main__":
    nums = [0, 1, 2, 5, 3, 3, 0]
    print(Solution().solutionOne(nums))
