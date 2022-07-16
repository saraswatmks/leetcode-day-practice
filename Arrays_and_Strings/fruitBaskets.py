"""
This is a sliding window approach question. Fixed window.
https://leetcode.com/problems/fruit-into-baskets/

Other words: Find the longest subarray with max 2 unique classes.

Input: fruits = [0,1,2,2]
Output: 3 # [1,2,2]

"""

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list):
        fruit_types = defaultdict(int)
        distinct = 0
        max_fruits = 0

        left = right = 0
        while right < len(fruits):
            # check if it is new fruit
            if fruit_types[fruits[right]] == 0:
                distinct += 1
            fruit_types[fruits[right]] += 1

            # too many different fruits, start shrinking the window
            while distinct > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    distinct -= 1
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits

    def totalFruit2(self, fruits: list):

        left = 0
        seen = defaultdict(int)

        for right in range(len(fruits)):
            seen[fruits[right]] += 1

            if len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
        return right - left + 1


if __name__ == "__main__":
    s = [1, 1, 2, 2, 3, 2, 2]
    sol = Solution().totalFruit2(s)
    print(sol)
