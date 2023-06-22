"""
This is similar to house robbers problem.

https://leetcode.com/problems/delete-and-earn/description/

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points

"""


class Solution:
    def solutionOne(self, nums: list):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        buckets = [0] * (max(nums) + 1)

        # add an number to its index, this will bucket the numbers
        for num in nums:
            buckets[num] += num

        dp = [0] * len(buckets)
        dp[1] = buckets[1]

        for i in range(2, len(buckets)):
            dp[i] = max(buckets[i] + dp[i - 2], dp[i - 1])

        return dp[len(dp) - 1]

    def solutionTwo(self, nums: list):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        buckets = [0] * (max(nums) + 1)

        # add an number to its index, this will bucket the numbers
        for num in nums:
            buckets[num] += num

        prev1 = 0
        prev2 = 0

        for i in range(len(buckets)):
            tmp = prev1
            prev1 = max(prev2 + buckets[i], prev1)
            prev2 = tmp

        return prev1


if __name__ == "__main__":
    nums = [2, 2, 3, 3, 3, 4]
    s = Solution().solutionOne(nums)
    print(s)
    s = Solution().solutionTwo(nums)
    print(s)
