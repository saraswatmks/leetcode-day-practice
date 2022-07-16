"""

This is sliding window question.

Find longest substring with atmost two.
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Input: s = "eceba"
Output: 3

"""


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Time Complexity: O(N)
        Space Complexity: O(1) - since hashmap will only have 3 char at most.
        """
        left = 0
        right = 0
        count = defaultdict(int)

        while right < len(s):
            count[s[right]] += 1
            right += 1

            if len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
        return right - left


if __name__ == "__main__":
    s = "ccaabbb"
    sol = Solution().lengthOfLongestSubstring(s)
    print(sol)
