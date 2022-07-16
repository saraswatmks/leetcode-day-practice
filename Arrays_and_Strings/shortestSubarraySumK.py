"""
Shortest subarray with sum atleast K.
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Input: nums = [2,-1,2], k = 3
Output: 3
"""


from collections import deque


class Solution:
    def shortestSubarrayOne(self, nums: list, k: int):
        """
        Sliding window implemented using dequeue.

        The idea is to maintain a monotonically increasing queue.
        If the curr_sum becomes lower, we remove the values from deque untill
        the lower value can be inserted.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # [index, sum]
        d = deque([[0, 0]])
        res, cur = float("inf"), 0

        for i, a in enumerate(nums):
            cur += a
            # diff is bigger than k
            while d and cur - d[0][1] >= k:
                res = min(res, i - d.popleft()[0] + 1)
            # remove values bigger than cur value.
            while d and cur <= d[-1][1]:
                d.pop()
            # append cur value in the end
            d.append([i + 1, cur])

        return res if res != float("inf") else -1


if __name__ == "__main__":
    nums = [2, 7, 3, -8, 4, 10]
    k = 12
    nums = [1]
    k = 1
    sol = Solution().shortestSubarrayOne(nums, k)
    print(sol)
