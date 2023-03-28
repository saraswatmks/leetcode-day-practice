"""
Asked in Bloomberg. 

https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

Given an int n. You can use only 2 operations:

    multiply by 2
    integer division by 3 (e.g. 10 / 3 = 3)

Find the minimum number of steps required to generate n from 1.

Input: 3
Output: 7
Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
"""


class Solution:
    def solutionOne(self, n: int):
        """
        This is BFS solution.
        Time Complexity: O(2^S) -> S is number of steps
        Space Complexity: O(S) -> S is number of steps (length of visited set)
        """
        q = [1]
        visited = {-1}
        depth = 0
        while q:
            q_size = len(q)
            for i in range(q_size):
                num = q.pop(0)
                if num == n:
                    return depth
                if num in visited:
                    continue
                visited.add(num)
                q.append(num * 2)
                q.append(num // 3)

            depth += 1

        return -1


if __name__ == "__main__":
    n = 3
    print(Solution().solutionOne(n))
