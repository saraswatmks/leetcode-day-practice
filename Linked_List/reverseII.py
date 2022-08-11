"""
Reverse a linked list between two given indexes.
https://leetcode.com/problems/reverse-linked-list-ii/

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetweenOne(head, left, right):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head or left == right:
            return head

        p = dummy = ListNode(None)
        dummy.next = head

        for i in range(left - 1):
            p = p.next

        tail = p.next

        for i in range(right - left):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        
        return dummy.next
