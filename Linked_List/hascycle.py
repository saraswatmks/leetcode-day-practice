"""
Check if ll has a cycle i.e. any node is pointing to previous nodes in the list
https://leetcode.com/problems/linked-list-cycle/solution/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode):
        """
        Using hashmap here.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: ListNode):
        """
        Using fast and slow pointer approach
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
