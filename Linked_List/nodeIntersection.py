"""
Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

listA = [1,9,1,2,4], listB = [3,2,4]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersection(headA, headB):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa
