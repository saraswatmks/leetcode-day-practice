"""
Find the continuous subarray that sums upto k.

Input: nums = [23,2,4,6,7], k = 6
Output: true

https://leetcode.com/problems/continuous-subarray-sum/
"""


class Solution:
    def checkSubarraySum(self, nums: list, k: int):
        """

        This approach is based on the fact:
            1. Get sum upto the number.
            2. Take mod of the sum % k
            3. Check if remainder was already encountered previously.

        Time Complexity: O(n)
        Space Complexity O(min(k, n))
        """
        d = {0: -1}
        # d = {}

        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            if k != 0:
                pre_sum = pre_sum % k
            # if the  sum of mod is already seen
            if pre_sum in d:
                if i - d[pre_sum] >= 2:
                    return True
            else:
                d[pre_sum] = i
        return False


if __name__ == "__main__":
    nums = [23, 2, 4, 6, 7]
    k = 6
    # sol = Solution().checkSubarraySum(nums, k)
    # print(sol)
    # nums = [24, 1, 1, 1, 1]
    nums = [1, 2, 4, 6]
    k = 6
    sol = Solution().checkSubarraySum(nums, k)
    print(sol)
