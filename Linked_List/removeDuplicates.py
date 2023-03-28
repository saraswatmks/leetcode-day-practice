"""
Remove duplicates from a sorted / unsorted list.
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicatesOne(self, head: ListNode):
        """
        From an sorted list.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        curr = head
        while curr:
            temp = curr
            while temp.next:
                if curr.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            curr = curr.next
        return head

    def removeDuplicatesTwo(self, head: ListNode):
        """
        From an un sorted list.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if not head:
            return None

        d = {}
        curr = head

        while curr:
            d[curr.val] = d.get(curr.val, 0) + 1
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head:
            if d[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next

    def removeDuplicatesThree(self, head: ListNode):
        """
        From a sorted list.
        Using hashmap.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # create a lookup map if a value is seen
        seen = set()
        curr = head
        seen.add(head.val)
        while curr.next:
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.val)
                curr = curr.next
        return head
