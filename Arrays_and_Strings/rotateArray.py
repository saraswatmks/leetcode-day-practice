"""
https://leetcode.com/problems/rotate-array/
Given an array, rotate it k times.

Input: nums = [1,2,3,4,5,6,7], k = 23
Output: [6,7,1,2,3,4,5]

"""


class Solution:
    def solutionOne(self, nums, k):
        """
        This is brute force.

        Time Complexity: O(n x k)
        Space Complexity: O(1)
        """
        n = len(nums)
        k = k % n
        for _ in range(k):
            prev = nums[-1]
            for i in range(n):
                tmp = nums[i]
                nums[i] = prev
                prev = tmp
        return nums

    def solutionTwo(self, nums, k):
        """
        This is using cyclic replacements.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                nxt = (current + k) % n
                tmp = nums[nxt]
                nums[nxt] = prev
                prev = tmp
                current = nxt
                count += 1

                if start == current:
                    break
            start += 1

        return nums

    def solutionThree(self, nums, k):
        """
        This is cyclic replacement but using my method.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)
        k = k % n

        current = 0
        prev = nums[current]

        for _ in range(n):
            nxt = (current + k) % n
            tmp = nums[nxt]
            nums[nxt] = prev
            prev = tmp
            current = nxt
        return nums


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 23
    nums = [1, 2, 3]
    k = 4
    print(Solution().solutionThree(nums, k))
