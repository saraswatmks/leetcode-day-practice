"""
This is a variable sliding window question.

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

from collections import Counter


class Solution:
    def solutionOne(self, s: str, t: str):
        """
        Time Complexity: O(m+n)
        Space Complexity: O(m+n)
        """
        target_letter_counts = Counter(t)
        start = 0
        end = 0
        min_window = ""
        target_len = len(t)

        for end in range(len(s)):
            # found a letter
            if target_letter_counts[s[end]] > 0:
                target_len -= 1

            # decrease the dict count
            target_letter_counts[s[end]] -= 1

            # if all letters in the target are found:
            while target_len == 0:
                window = end - start + 1
                if not min_window or window < len(min_window):
                    # new window
                    min_window = s[start : end + 1]

                # increase the letter count, for future coming windows
                target_letter_counts[s[start]] += 1

                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_letter_counts[s[start]] > 0:
                    target_len += 1

                start += 1

        return min_window


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = print(Solution().solutionOne(s, t))
    print(sol)
