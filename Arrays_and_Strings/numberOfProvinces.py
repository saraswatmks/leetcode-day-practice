"""
This is a graph problem.

Count the number of connected provinces. 
https://leetcode.com/problems/number-of-provinces/description/

Input: isConnected = 
[[1,1,0],
 [1,1,0],
 [0,0,1]
]
Output: 2

"""


class Solution:
    def solutionOne(self, mat):
        """
        DFS.

        Time Complexity: O(n * n) <- length * breadth of matrix
        Space Complexity: O(n)
        """

        if not mat:
            return 0

        s = len(mat)
        seen = set()
        cnt = 0

        def dfs(i):
            # val is the value of each node's connection with other nodes in adjacency list
            for q, val in enumerate(mat[i]):
                if val == 1 and q not in seen:
                    seen.add(q)
                    dfs(q)

        # each row denotes the adjacency list of a graph node
        # that's why we iterate only across rows
        for i in range(len(mat)):
            if i not in seen:
                dfs(i)
                cnt += 1

        return cnt


if __name__ == "__main__":
    # each row denotes the adjacency list of a graph node
    m = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().solutionOne(m))
