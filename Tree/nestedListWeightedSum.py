"""
Return  sum of each list multiplied by depth
https://leetcode.com/problems/nested-list-weight-sum/

Input: nestedList = [[1,1],2,[1,1]]
Output: 10 (1 * 2 + 1* 2 + 2*1 + 1 * 2 + 1* 2)

Input: nestedList = [1,[4,[6]]]
Output: 27 (1*1 + 2 * 4 + 3 * 6)

"""
from collections import deque


class Solution:
    def depthSumOne(self, s):
        """
        DFS approach.
        Time Complexity: O(n)
        Space Complexity: O(d) d -> depth

        """

        def _dfs(s, depth):
            total = 0
            for i in s:
                if isinstance(i, int):
                    total += i * depth
                elif isinstance(i, list):
                    total += _dfs(i, depth + 1)

            return total

        depth = 1
        return _dfs(s, depth)

    def depthSumTwo(self, s):
        """
        BFS Approach.
        Time Complexity: O(n)
        Space Complexity: O(m) -> m -> max number of elements at a given level
        """
        queue = deque(s)
        depth = 1
        total = 0
        while len(queue) > 0:
            # since the queue is getting modified from inside, this ensure the loop doesn't run forever
            size = len(queue)
            for i in range(size):
                nested = queue.pop()
                if isinstance(nested, int):
                    total += depth * nested
                elif isinstance(nested, list):
                    queue.extendleft(nested)
            depth += 1
        return total


if __name__ == "__main__":
    s = [1, [4, [6]]]
    sol = Solution().depthSumOne(s)
    print(sol)
    s = [[1, 1], 2, [1, 1]]
    sol = Solution().depthSumTwo(s)
    print(sol)
