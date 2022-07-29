"""
Find middle node of the linked list
https://leetcode.com/problems/middle-of-the-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode):
        """
        Time complexity: O(n/2) -> O(n)
        Space complexity: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNodeTwo(self, head: ListNode):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        def _getLength(node):
            ans = 0
            while node:
                ans += 1
                node = node.next
            return ans

        node_len = _getLength(head)
        mid = node_len // 2

        # move to the mid node
        cnt = 0
        while cnt < mid:
            head = head.next
            cnt += 1

        return head
