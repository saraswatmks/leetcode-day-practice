"""
Given a list of parents where index of each parent is it node value, count the nodes.

https://leetcode.com/problems/count-nodes-with-the-highest-score/description/

Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
"""
from collections import defaultdict
class Solution:
    def solutionOne(self, parents):
        """
        DFS Solution
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        children = defaultdict(list)

        for node, parent in enumerate(parents):
            children[parent].append(node)
        
        freq = defaultdict(int)
        NODES = len(parents)
        
        def dfs(node):
            # think in terms of left, right and up direction of the tree
            # when we remove the node, its left subtree, right subtree and upper part of the tree are left loose
            left = right = 0
            if children[node]:
                left = dfs(children[node][0])
            if len(children[node])> 1:
                right = dfs(children[node][1])
            # these many nodes available after removing the current node
            up = NODES - left - right - 1
            score = (left or 1) * (right or 1) * (up or 1)
            freq[score] += 1
            return 1 + left + right


        dfs(0)
        return freq[max(freq)]

if __name__ == "__main__":
    parents = [-1,2,0,2,0]
    print(Solution().solutionOne(parents))