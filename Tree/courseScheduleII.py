"""
This is a graph question. 

https://leetcode.com/problems/course-schedule-ii/description/

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

"""
from collections import defaultdict


class Solution:
    def solutionOne(self, numCourses, prerequisites):
        """
        Time Complexity: O(N+E) N -> nodes, E -> Edges
        Space Complexity: O(N+E)
        """
        G = defaultdict(list)
        q = []
        ans = []
        indegree = [0] * numCourses

        for nxt, pre in prerequisites:
            # {0: [1,2]} 0 is a prerequisite of 1 and 2
            G[pre].append(nxt)
            indegree[nxt] += 1  # number of incoming edges for a node

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)  # start node, it doesn't have any incoming nodes

        while q:
            curr = q.pop(0)
            ans.append(curr)

            for nxtcourse in G[curr]:
                indegree[nxtcourse] -= 1
                if indegree[nxtcourse] == 0:
                    q.append(nxtcourse)  # push next node to the queue

        if len(ans) != numCourses:
            return []

        return ans


if __name__ == "__main__":
    numCourses = 3
    # numCourses = 4
    # prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    s = Solution().solutionOne(
        numCourses=numCourses, prerequisites=prerequisites
    )
    print(s)
