"""
Find maximum sum from subarray of size k

Input: nums = [1,2,3,4,5], k = 2
Output: 9

"""


class Solution:
    def subArraySumThree(self, nums: list, k):
        """
        This is using a fixed sliding window. This is using while loop.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = j = 0
        res = 0
        curr_sum = 0

        while j < len(nums):
            curr_sum += nums[j]
            # j-i+1 keeps the window fixed.
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                res = max(res, curr_sum)
                # here we remove the ith value from sum, to avoid repeat summing.
                curr_sum -= nums[i]
                i += 1
                j += 1

        return res

    def subArraySumThree2(self, nums: list, k):
        """
        This is using a fixed sliding window. This is using for loop.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = j = 0
        res = 0
        curr_sum = 0

        for j in range(len(nums)):
            curr_sum += nums[j]
            print(f"window: π", end='\n\n')
            if j - i + 1 >= k:
                res = max(res, curr_sum)
                # here we remove the ith value from sum, to avoid repeat summing.
                curr_sum -= nums[i]
                i += 1

        return res


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 1, 1, 3, 4, 1, 5]
    k = 3
    sol = Solution().subArraySumThree(nums, k)
    print(sol)
    sol = Solution().subArraySumThree2(nums, k)
    print(sol)
