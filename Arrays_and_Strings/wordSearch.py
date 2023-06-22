"""
Find a word in the given 2D array (matrix).
https://leetcode.com/problems/word-search/

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

"""


class Solution:
    def wordSearchOne(self, board, word):
        """
        Time Complexity: O(M * N * 4 ^ s) s -> s is len of word
        """
        rows = len(board)
        cols = len(board[0])

        def backtrack(board, row, col, word):
            # word is found
            if len(word) == 0:
                return True
            # no point in going ahead, exit.
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != word[0]
                or board[row][col] == "#"
            ):
                return False

            char = board[row][col]
            # to avoid visiting again
            board[row][col] = "#"
            down = backtrack(board, row + 1, col, word[1:])
            up = backtrack(board, row - 1, col, word[1:])
            left = backtrack(board, row, col - 1, word[1:])
            right = backtrack(board, row, col + 1, word[1:])
            ans = up or down or left or right
            board[row][col] = char
            return ans

        for row in range(rows):
            for col in range(cols):
                if backtrack(board, row, col, word):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution().wordSearchOne(board, word)
    print(sol)
