"""
Remove given elements from the linked list.
https://leetcode.com/problems/remove-linked-list-elements/

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# val = 2
# 1 > 2 > 3 > 4
# 1 > 3 > 4


class Solution:
    def removeElements(self, head: ListNode, val: int):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
