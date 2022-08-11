"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

https://leetcode.com/problems/combinations/

"""


class Solution:
    def combineOne(self, n: int, k: int):
        """
        Using dfs approach

        Time Complexity: O(nCk) -> n! / k! * (n-k)!
        Space Complexity: O(nCk) -> n! / k! * (n-k)!

        """

        def dfs(start, tmp):
            if len(tmp) == k:
                output.append(tmp[:])

            for i in range(start, n + 1):
                dfs(i + 1, tmp + [i])

        output = []
        start = 1
        dfs(start, [])
        return output

    def combineTwo(self, n: int, k: int):
        """
        Using backtracking approach.

        Time Complexity: O(nCk) -> n! / k! * (n-k)!
        Space Complexity: O(nCk) -> n! / k! * (n-k)!
        """

        def backtrack(start, tmp):
            if len(tmp) == k:
                output.append(tmp[:])

            for i in range(start, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp)
                tmp.pop()

        output = []
        backtrack(1, [])
        return output


if __name__ == "__main__":
    n = 4
    k = 2
    sol = Solution().combineOne(n, k)
    print(sol)
    sol = Solution().combineTwo(n, k)
    print(sol)
