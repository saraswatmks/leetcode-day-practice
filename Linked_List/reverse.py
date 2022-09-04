"""
Reverse a linked list.
https://leetcode.com/problems/reverse-linked-list/
"""


# 1 > 2 > 3 > 4 > 5 -> null
#

from utils import list_to_link, ListNode

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
        # here head points to the original head
        # connects 5 <- 4<- 3 <- 2 to 1
        head.next.next = head
        head.next = None
        return p

    def reverseListRecursiveTwo(self, head: ListNode):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """

        def solve(head, curr, prev):
            # when we reach the end, we set the prev to head
            # since that is going to be the first valid node from the end.
            if not curr:
                head = prev
                return

            forward = curr.next
            solve(head, forward, curr)
            curr.next = prev

        prev = None
        curr = head
        solve(head, curr, prev)
        return head


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    ll = list_to_link(l)
    s = Solution().reverseListRecursive(ll)
    print(s)
    s = Solution().reverseListRecursiveTwo(ll)
    print(s)
