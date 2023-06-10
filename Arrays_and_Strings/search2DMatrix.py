"""
Given a 2D matrix, check if the target exists.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


class Solution:
    def solutionOne(self, matrix, target):
        """
        Time Complexity: Ologn + Ologm
        Space Complexity: O(1)
        """

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1

        # iterate through rows and find which row can have target
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        row_index = high
        low = 0
        high = cols - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def solutionTwo(self, matrix, target):
        """
        Using binary search.
        Time Complexity: O(log m*n)
        Space Complexity: O(1)
        """
        if not matrix or not target:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            # row col index
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 60
    s = Solution().solutionOne(matrix, target)
    print(s)
