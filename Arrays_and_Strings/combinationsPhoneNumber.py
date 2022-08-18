"""

Find all the combination of letters given a digit.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""


class Solution:
    def letterCombinations(self, digits):
        """
        This is a backtracking question. Using dfs.

        Time Complexity: O(4 ^ N)
            Here 4 refers to the max digit on number 7 (pqrs) and 9 (wxyz)
            N -> length of digits

        Space Complexity: O(N)

        """

        res = []
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, tmp):
            if len(tmp) == len(digits):
                res.append("".join(tmp[:]))
                return

            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                tmp.append(letter)
                backtrack(index + 1, tmp)
                tmp.pop()

        backtrack(0, [])
        return res

    def letterCombinationdfs2(self, digits: str):
        """
        This is a backtracking question. Using dfs.

        Time Complexity: O(4 ^ N)
            Here 4 refers to the max digit on number 7 (pqrs) and 9 (wxyz)
            N -> length of digits

        Space Complexity: O(N)

        """

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(nums: str, index: int, path: str):
            if index >= len(nums):
                res.append(path)
                return

            string1 = dic[nums[index]]
            for s in string1:
                dfs(nums, index + 1, path + s)

        dfs(digits, 0, "")
        return res


if __name__ == "__main__":
    digits = "23"
    sol = Solution().letterCombinations(digits)
    print(sol)
    sol = Solution().letterCombinationdfs2(digits)
    print(sol)
