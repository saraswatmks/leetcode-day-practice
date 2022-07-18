"""
Given a matrix with zeroes, mark its entire corresponding row and cols with zero.
https://leetcode.com/problems/set-matrix-zeroes/

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""


class Solution:
    def setZeroes(self, matrix):
        """
        Time Complexity: O(M X N)
        Time Complexity: O(M + N)
        """
        R = len(matrix)
        C = len(matrix[0])

        row, col = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(R):
            for j in range(C):
                if i in row or j in col:
                    matrix[i][j] = 0

        return matrix

if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol = Solution().setZeroes(matrix)
    print(sol)
