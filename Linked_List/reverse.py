"""
Reverse a linked list.
https://leetcode.com/problems/reverse-linked-list/
"""


# 1 > 2 > 3 > 4 > 5 -> null
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements."""
    if len(lst) == 1:
        return ListNode(lst[0])
    return ListNode(lst[0], list_to_link(lst[1:]))  # <<<< RECURSIVE


class Solution:
    def reverseList(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseListRecursive(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # base case
        if not head or not head.next:
            return head

        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    ll = list_to_link(l)
    s = Solution().reverseListRecursive(ll)
    print(s)
