"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        def flattenTree(self, node):
            if not node:
                return

            # this is leaf node
            if not node.left and not node.right:
                return node

            # keep going left
            leftTail = flattenTree(node.left)

            # keep going right
            rightTail = flattenTree(node.right)

            # mean there's a node found at left
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail or leftTail

        return flattenTree(root)

    def flattenTwo(self, root):
        """
        This is Morris Traversal. Using constance space.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not root:
            return

        curr = root

        # check if node exists
        while curr:

            # check if left node to the root exists
            while curr.left:
                prev = curr.left
                # then keep going towards the right child of the left node
                while prev.right:
                    prev = prev.right

                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right

        return root

    def flattenThree(self, root):
        """
        This is using recursion. Reverse Preorder Traversal (RLN)

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        prev = None
        def flatten(node):
            nonlocal prev
            if not node:
                return
            flatten(node.right)
            flatten(node.left)
            node.right = prev
            node.left = None
            prev = node
    
        flatten(root)
        return root