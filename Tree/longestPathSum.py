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
    root = Node(4)  #     4
    root.left = Node(2)  #     / \
    root.right = Node(5)  #     2 5
    root.left.left = Node(7)  #     / \ / \
    root.left.right = Node(1)  # 7 1 2 3
    root.right.left = Node(2)  #     /
    root.right.right = Node(3)  #     6
    root.left.right.left = Node(6)
    return root

# TODO: Incomplete
class Solution:
    def longestPathOne(self, root: Node):

        maxdepth = 0
        depth = 0
        curr_sum = 0
        maxSum = -1 * sys.maxsize

        def getMax(root, maxdepth, depth, curr_sum):
            nonlocal maxSum
            # base case
            if not root:
                if depth > maxdepth:
                    # new depth and new sum
                    maxdepth = depth
                    maxSum = curr_sum
                elif depth == maxdepth and curr_sum >= maxSum:
                    maxSum = max(curr_sum, maxSum)
                return

            curr_sum = root.data + curr_sum
            getMax(root.left, maxdepth, depth + 1,  curr_sum)
            getMax(root.right, maxdepth, depth + 1,  curr_sum)

        getMax(root, maxdepth, depth, curr_sum)
        return maxSum


if __name__ == "__main__":
    root = create_tree()
    sol = Solution().longestPathOne(root)
    print(sol)
