"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

https://leetcode.com/problems/max-number-of-k-sum-pairs/description

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
"""


class Solution:
    def solutionOne(self, nums, k):
        """
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            for j in range(1 + 1, len(nums)):
                if nums[j] == -1:
                    continue
                if nums[i] + nums[j] == k:
                    count += 1
                    nums[i] = -1
                    nums[j] = -1
                    break
        return count

    def solutionTwo(self, nums, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dct = {}
        cnt = 0
        for i in nums:
            # if diff = k - num is found, means we have atleast one pair
            if dct.get(k - i, 0) != 0:
                dct[k - i] -= 1
                cnt += 1
            else:
                dct[i] = dct.get(i, 0) + 1
        return cnt

    def solutionThree(self, nums, k):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1

        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == k:
                count += 1
                i += 1
                j -= 1
            elif tmp > k:
                j -= 1
            else:
                i += 1
        return count


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5
    s = Solution().solutionThree(nums, k)
    print(s)
