"""
Remove duplicates from a sorted / unsorted list.
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicatesOne(self, head: ListNode):
        """
        From an unsorted list.

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
        From a sorted list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        pass

    def removeDuplicatesThree(self, head: ListNode):
        """
        From an unsorted list.
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
