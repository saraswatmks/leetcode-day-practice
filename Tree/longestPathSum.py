"""
Find the sum of all nodes on the longest path from root to leaf node
https://www.geeksforgeeks.org/sum-nodes-longest-path-root-leaf-node/

Input : Binary tree:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output : 13

"""

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    # binary tree formation
    root = Node(4)  #                  4
    root.left = Node(2)  #            / \
    root.right = Node(5)  #           2 5
    root.left.left = Node(7)  #      / \ / \
    root.left.right = Node(1)  #     7 1 2 3
    root.right.left = Node(2)  #       /
    root.right.right = Node(3)  #      6
    root.left.right.left = Node(6)
    return root


# TODO: Incomplete
class Solution:
    def longestPathOne(self, root: Node):

        """Recursive Solution."""

        maxdepth = 0
        maxSum = -1 * sys.maxsize

        def getMax(node, depth, curr_sum):
            nonlocal maxSum, maxdepth
            # base case - if node is empty
            if not node:
                # 1st criteria - depth should be max
                if depth > maxdepth:
                    # new depth and new sum
                    maxdepth = depth
                    maxSum = curr_sum
                # 2nd criteria - if depth same, check if max sum
                elif depth == maxdepth and curr_sum >= maxSum:
                    maxSum = curr_sum
                return

            getMax(node.left, depth + 1, node.data + curr_sum)
            getMax(node.right, depth + 1, node.data + curr_sum)

        getMax(root, 0, 0)
        return maxSum

    def longestPathTwo(self, root: Node):
        """
        Level Order Traversal
        Time Complexity: O(n)
        Space Complexity: O(l) -> l is max. no. of nodes in a level
        """
        if not root:
            return 0

        maxSum = root.data
        maxdepth = 0

        q = []
        q.append((root, 0, root.data))

        while q:
            curr, depth, node_sum = q.pop(0)
            if depth > maxdepth:
                maxdepth = depth
                maxSum = node_sum
            elif depth == maxdepth and node_sum > maxSum:
                maxSum = node_sum

            if curr.left:
                q.append((curr.left, depth + 1, curr.left.data + node_sum))

            if curr.right:
                q.append((curr.right, depth + 1, curr.right.data + node_sum))

        return maxSum


if __name__ == "__main__":
    root = create_tree()
    # sol = Solution().longestPathOne(root)
    # print(sol)
    sol2 = Solution().longestPathTwo(root)
    print(sol2)
