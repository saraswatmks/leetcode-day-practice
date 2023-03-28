"""
Find subarray equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Input: nums = [1,2,3], k = 3
Output: 2 # [[1,2], [3]]

"""


class Solution:
    def subArraySumOne(self, nums: list, k):
        """
        Time Complexity: O(n2)
        Space Complexity: O(n)
        """
        count = 0
        cumSum = [0] * (len(nums) + 1)
        #  we need to leave 0 at 0 index.
        # Here's the explanation: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
        cumSum[1] = nums[0]

        for i in range(2, len(nums) + 1):
            cumSum[i] = cumSum[i - 1] + nums[i - 1]

        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                # print(f"{cumSum[j]=} - {cumSum[i]=}")
                if cumSum[j] - cumSum[i] == k:
                    count += 1

        return count

    def subArraySumTwo(self, nums: list, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        d = {}
        # hack to fill values when 0 difference is found
        d[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum = curr_sum + num
            diff = curr_sum - k
            count += d.get(diff, 0)
            d[curr_sum] = d.get(curr_sum, 0) + 1

        return count


if __name__ == "__main__":
    nums = [1, 3, 2, 1, 3]
    k = 3
    # sol = Solution().subArraySumOne(nums, k)
    sol = Solution().subArraySumTwo(nums, k)
    print(sol)
    # nums = [1, -1, 0]
    # k = 0
    # sol = Solution().subArraySumTwo(nums, k)
    # print(sol)
