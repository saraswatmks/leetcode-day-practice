"""
Find longest sequence length in the array
https://leetcode.com/problems/longest-consecutive-sequence/

Input: [100,4,200,1,3,2]
Output: 4  # 1,2,3,4

"""


class Solution:
    def longestSequence(self, nums: list):
        """
        TLE Exceeded.
        Time Complexity: O(n) n -> max_number
        Space Complexity: O(1)
        """
        start = 0
        maxs = max(nums)

        max_ans = 0
        ans = 0
        while start <= maxs:
            if start in nums:
                ans += 1
            else:
                max_ans = max(max_ans, ans)
                ans = 0

            start += 1

        return max(max_ans, ans)

    def longestSequence2(self, nums: list):
        """
        Time Complexity: O(n3)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        max_ans = 0
        ans = 0

        for num in nums:
            start = num
            while start in nums:
                start += 1
                ans += 1
            max_ans = max(max_ans, ans)
            ans = 0
        return max_ans

    def longestSequence3(self, nums: list):
        """
        Using sort
        Time Complexity: O(nlogn)
        Space Complexity: O(n)

        """
        if not nums:
            return 0

        nums = nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)

    def longestSequence4(self, nums):
        """
        Using hashmap.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_len = 1
                while current_num + 1 in nums:
                    current_num += 1
                    current_len += 1
                longest = max(longest, current_len)
        return longest


if __name__ == "__main__":
    # s1 =  [100,4,200,1,3,2]
    s2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 99999]
    # print(Solution().longestSequence(s1))
    print(Solution().longestSequence(s2))
    print(Solution().longestSequence2(s2))
    print(Solution().longestSequence3(s2))
