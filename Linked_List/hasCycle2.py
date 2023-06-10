"""
Return the node where cycle starts.
https://leetcode.com/problems/linked-list-cycle-ii/description/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""


class Solution:
    def solutionOne(self, head):
        """
        Idea is to follow:
        1. Start with a slow and fast pointer iterate until they meet where cycle ends.
        2. Change the speed of fast pointer and iterate until they meet at cycle start point.

        Time Complexity: O(n)
        Space Complexity: O(1)

        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # pointers have met where cycle ends
                slow = head
                while (
                    slow != fast
                ):  # iterate until pointers meet where cycle starts
                    slow = slow.next
                    fast = fast.next
                return slow
