"""
This is a graph question.

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

"""

from collections import defaultdict, deque


class Solution:
    def solutionOne(self, n, connections):
        """
        Main idea is to count number of outgoing edges from 0 and its neighbours
        """
        res = 0
        visited = {0}
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))  # 1 is the cost of going outwards
            graph[v].append((u, 0))  # 0 cost of going inwards

        def dfs(city):
            nonlocal res, visited, graph, connections

            for nei, cost in graph[city]:
                if nei not in visited:
                    visited.add(nei)
                    res += cost
                    dfs(nei)

        dfs(0)
        return res

    def solutionTwo(self, n, connections):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))

        q = deque([0])
        visited = set([0])
        num_changes = 0

        while q:
            curr = q.popleft()
            for child, cost in graph[curr]:
                if child not in visited:
                    visited.add(child)
                    num_changes += cost
                    q.append(child)

        return num_changes


if __name__ == "__main__":
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    s = Solution().solutionOne(n, connections)
    print(s)
