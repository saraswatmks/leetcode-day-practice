"""
Find average of top 5 marks scored by a student.
https://leetcode.com/problems/high-five/discuss/312443/Python-Sort-or-Priority-Queue-solution

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
"""

import heapq
from collections import defaultdict


class Solution:
    def highFiveOne(self, items):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        items.sort(reverse=True)
        idx = items[0][0]
        res = []
        curr = []

        for student, marks in items:
            if student == idx:
                if len(curr) < 5:
                    curr.append(marks)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [marks]
                idx = student

        res.append([idx, sum(curr) // len(curr)])
        res = res[::-1]
        return res

    def highFiveTwo(self, items):
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        d = defaultdict(list)

        for idx, val in items:
            heapq.heappush(d[idx], val)

            if len(d[idx]) > 5:
                heapq.heappop(d[idx])

        print(f"this is d: {d}")
        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]
        return res


if __name__ == "__main__":
    items = [
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [2, 77],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ]
    sol = Solution().highFiveOne(items)
    print(sol)
    sol = Solution().highFiveTwo(items)
    print(sol)
