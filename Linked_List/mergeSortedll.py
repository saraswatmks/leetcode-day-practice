"""
Merge the two sorted linked lists.
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1 -> 2 -> 4
# 1 -> 3 -> 4
# 1 > 1 > 2 > 3 > 4 > 4


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        Time complexity: O(n + m)
        Space complexity: O(1)
        """
        dummy = ListNode(-1)
        prev = dummy

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

        prev.next = list1 or list2
        return dummy.next

    def mergeWithRecursion(self, list1: ListNode, list2: ListNode):
        """
        Time complexity: O(n+m)
        Space complexity: O(n+m)
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeWithRecursion(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeWithRecursion(list1, list2.next)
            return list2
