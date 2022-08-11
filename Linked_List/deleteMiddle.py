"""
Find middle node of the linked list
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head.next:
            return head.next

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # skip (or delete the pointer) the found middle node.
        slow.next = slow.next.next
        return head
