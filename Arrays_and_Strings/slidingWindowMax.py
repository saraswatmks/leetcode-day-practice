"""
Given an array, find the max in each sliding window.
https://leetcode.com/problems/sliding-window-maximum/description/

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
import collections


class Solution:
    def solutionOne(self, nums: list, k: int):
        """
        We use a deque (to store indexes) and a stack (to store answer).
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        d = collections.deque()
        ans = []

        for i, num in enumerate(nums):
            # check if ans has largest numbers
            while d and nums[d[-1]] < num:
                d.pop()

            # check if window size is not crossed
            if d and i - d[0] >= k:
                d.popleft()

            d.append(i)
            ans.append(nums[d[0]])  # append leftmost index to ans

        return ans[k - 1 :]

    def solutionTwo(self, nums: list, k: int):
        """
        Same approach as above solution, just slight changes in implementation
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # length of q will always be equal to k
        q = collections.deque()
        ans = []

        for i, num in enumerate(nums):
            # remove lower number
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(i)
            # remove index if outside window
            if (
                q and q[0] == i - k
            ):  # 2 ==2 (window size will be 3 since 0,1,2)
                q.popleft()

            # start collecting answer only after first window is crossed
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    nums = [1, 5, 4, 3, 2, 1, 6, 7]
    k = 3
    s = Solution().solutionOne(nums, k)
    print(s)
    s = Solution().solutionTwo(nums, k)
    print(s)
