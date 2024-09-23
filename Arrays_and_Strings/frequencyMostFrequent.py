"""
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.


Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
"""


class Solution:
    def solutionOne(self, nums, k):
        """
        Using sorting

        TC: O(n log n)
        SC: O(1)
        """
        left = right = total = res = 0
        nums.sort()

        while right < len(nums):
            total += nums[right]
            # this is the key idea
            # nums[right] * (right - left + 1) <- make all numbers same as nums[right]
            # k * total <- checks if we increase the total by k in the window above, would it still be fine
            while nums[right] * (right - left + 1) > k * total:
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == "__main__":
    ans = Solution().solutionOne([1, 4, 8, 13], 5)
    print(ans)
