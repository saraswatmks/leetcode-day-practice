"""
Validate a given binary search tree.

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Input: root = [5,1,4,null,null,3,6]
Output: false

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def validateTreeOne(self, root: TreeNode):
        """
        Using inorder traversal

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        output = []
        def inOrder(node, output):
            if not node:
                return
            inOrder(node.left, output)
            output.append(node.val)
            inOrder(node.right, output)
        # this fills the output list with inorder traversal values from the tree
        inOrder(root, output)

        # check if the order is valid
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        
        return True
    
    def validateTreeTwo(self, root: TreeNode):
        """
        Follows a strategy to track upper and lower bound at each node.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """


        def isvalid(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            # for left, the upper limit is the root node val
            # for right, the lower limit is the root node val.
            return isvalid(root.left, low, root.val) and isvalid(root.right, root.val, high)
            

        return isvalid(root, float("-inf"), float("inf"))


    def validateTreeThree(self, root: TreeNode):
        """
        Follows a bottom up strategy. In order traversal.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        prev = None
        def dfs(node):
            if not node:
                return True
            
            if not dfs(node.left):
                return False

            if prev and node.val <= prev:
                return False
            prev = node.val
            return dfs(node.right)

        return dfs(root)




        