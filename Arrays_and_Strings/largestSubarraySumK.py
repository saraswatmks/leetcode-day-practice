"""
Find maximum sum from subarray of size k

Input : { 10, 5, 2, 7, 1, 9 },  k = 15
Output : 4 # (5, 2, 7, 1)

"""


class Solution:
    def largestSubarray(self, nums: list, k):
        """
        This is using a variable sliding window .
        This approach only works for arr with positive numbers.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = j = 0
        res = 0
        cur_sum = 0

        while j < len(nums):
            cur_sum += nums[j]
            if cur_sum < k:
                j += 1
            else:
                if cur_sum == k:
                    res = max(res, j - i + 1)
                elif cur_sum > k:
                    while cur_sum > k:
                        cur_sum -= nums[i]
                        i += 1
                j += 1
        return res

    def largestSubarrayTwo(self, nums: list, k):
        """
        The idea is to store the cumulative difference.
        Then check if cum_sum - k is seen before, that means
        the distance between before value and current index must be k.


        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # store cumulative sum
        cum_dict = {}
        cur_sum = 0
        maxLen = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            temp = cur_sum - k
            if cur_sum == k:
                maxLen = i + 1
            elif temp in cum_dict:
                maxLen = max(maxLen, i - cum_dict[temp])
            if cur_sum not in cum_dict:
                cum_dict[cur_sum] = i

        return maxLen


if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    # sol = Solution().largestSubarray(nums, k)
    # print(sol)
    nums = [-5, 8, -14, 2, 4, 12]
    k = -5
    sol = Solution().largestSubarrayTwo(nums, k)
    print(sol)
