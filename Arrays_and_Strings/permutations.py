"""
Find permutations of the given array.
https://leetcode.com/problems/permutations

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permutewithbacktrack(self, nums: list):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                # [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
                print(f"{i=}, {nums=}, {first=}, {output=}")
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
                # this line is doing backtracking

        n = len(nums)
        output = []
        backtrack()
        return output

    def permutewithdfs(self, nums):
        """
        This solution uses dfs.

        Time Complexity: O(N * N!)
            N! is due to N * N-1 * N - 2 depth computation
            N is traversing through main array.
        Space Complexity: O (N!)
        """

        def _dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                pick_num = path + [nums[i]]
                without_num = nums[:i] + nums[i + 1 :]
                # print(f"{i=}, {pick_num=}, {without_num=}, {res=}")
                _dfs(without_num, pick_num, res)

        res = []
        _dfs(nums, [], res)
        return res

    def permutewithdfs2(self, nums):
        res = []
        def dfs(nums, tmp, res):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], tmp + [nums[i]], res)

        dfs(nums, [], res)
        return res

# draw tree 

# permutewithdfs(nums=[1, 2, 3])
# └── _dfs(nums=[1, 2, 3], path=[], res=[])
#     ├── _dfs(nums=[2, 3], path=[1]n, res=[])
#     │   ├── _dfs(nums=[3], path=[1, 2], res=[])
#     │   │   └── _dfs(nums=[], path=[1, 2, 3], res=[[1, 2, 3]])
#     │   └── _dfs(nums=[2], path=[1, 3], res=[])
#     │       └── _dfs(nums=[], path=[1, 3, 2], res=[[1, 3, 2]])
#     ├── _dfs(nums=[1, 3], path=[2], res=[])
#     │   ├── _dfs(nums=[3], path=[2, 1], res=[])
#     │   │   └── _dfs(nums=[], path=[2, 1, 3], res=[[2, 1, 3]])
#     │   └── _dfs(nums=[1], path=[2, 3], res=[])
#     │       └── _dfs(nums=[], path=[2, 3, 1], res=[[2, 3, 1]])
#     ├── _dfs(nums=[1, 2], path=[3], res=[])
#     │   ├── _dfs(nums=[2], path=[3, 1], res=[])
#     │   │   └── _dfs(nums=[], path=[3, 1, 2], res=[[3, 1, 2]])
#     │   └── _dfs(nums=[1], path=[3, 2], res=[])
#     │       └── _dfs(nums=[], path=[3, 2, 1], res=[[3, 2, 1]])
#     └── res=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


if __name__ == "__main__":
    nums = [1, 2, 3]
    # sol = Solution().permutewithdfs(nums)
    # print(sol)
    sol = Solution().permutewithbacktrack(nums)
    print(sol)
