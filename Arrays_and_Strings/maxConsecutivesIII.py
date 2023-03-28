"""
This is a sliding window based question. 

Return max consecutive ones, when we can flip max k 0s.
https://leetcode.com/problems/max-consecutive-ones-iii/

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

"""


class Solution:
    def longestOnes(self, nums: list, K: int):
        """
        Sliding window approach.
        Visual explanation: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                K -= 1

            if K < 0:
                if nums[left] == 0:
                    K += 1
                left += 1

        return right - left + 1


if __name__ == "__main__":
    # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    nums = [1, 1, 1, 0, 0, 0, 1]
    k = 2
    sol = Solution().longestOnes(nums, k)
    print(sol)
