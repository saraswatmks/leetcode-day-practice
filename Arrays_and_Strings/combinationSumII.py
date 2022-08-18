"""
This is a backtracking question.

Given a list of integers, find the combination of nums which sum up to the target value.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:
    def combinationSumOne(self, nums, target):
        """
        Time Complexity: O(2^n)
        Space Complexity: O(2^n)
            n -> length of nums
        """

        res = []

        def dfs(remain, arr, tmp):
            if remain < 0:
                return
            elif remain == 0:
                res.append(tmp[:])
                return

            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                dfs(remain - arr[i], arr[i + 1 :], tmp + [arr[i]])

        nums.sort()
        dfs(target, nums, [])
        return res


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sol = Solution().combinationSumOne(candidates, target)
    print(sol)
