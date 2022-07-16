"""
Find middle node of the linked list
https://leetcode.com/problems/middle-of-the-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
