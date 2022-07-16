"""

Find words formed by same char.
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6 # cat + hat

"""

from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        """
        Time Complexity: O(N * K)
        Space Complexity: O(1) since 26 chars max. (can be considered as constant)
        """
        res = 0
        chars_count = Counter(chars)

        for word in words:
            word_counter = Counter(word)

            for char in word_counter:
                if word_counter[char] > chars_count[char]:
                    break
            else:
                res += len(word)
        return res


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    sol = Solution().countCharacters(words, chars)
    print(sol)
