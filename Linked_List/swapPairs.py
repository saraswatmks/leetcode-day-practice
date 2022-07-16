"""
Swap adjacent nodes in a linked list
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next
        return dummy.next
