"""
Reverse a linked list between the given indexes.

https://leetcode.com/problems/reverse-linked-list-ii/solution/

Input: 1 -> 2 -> 3 -> 4 , m = 1, n = 3
Output: 1 -> 4 -> 3 -> 2
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n:int):
        if m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # reach the start point
        for i in range(m-1):
            pre = pre.next
        
        curr = pre.next
        nxt = curr.next

        for i in range(n - m):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        
        pre.next.next = nxt
        pre.next = curr
        return dummy.next
        


