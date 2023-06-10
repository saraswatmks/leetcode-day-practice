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
        Space Complexity: O(M + N)
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

    def solutionTwo(self, matrix):
        """
        Idea is to manually set if first row, col has zero, do it firstly.
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0

        return matrix


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # sol = Solution().setZeroes(matrix)
    sol = Solution().solutionTwo(matrix)
    print(sol)
