"""
Given a circular sorted linked list, insert into it
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
"""

from utils import ListNode, list_to_link, print_ll


class Solution:
    def insert(self, head: ListNode, insertVal: int):

        node = ListNode(insertVal)
        if not head:
            # create a circular list
            node.next = node
            return node

        prev, curr = head, head.next

        # go on till we are back to start
        while prev.next != head:

            # Case1: 1 <- 2 <- 3
            if prev.val <= node.val <= curr.val:
                break

            # Case2: tail node, increasing vals
            if prev.val > curr.val and (
                node.val > prev.val or node.val < curr.val
            ):
                break

            prev, curr = prev.next, curr.next

        # Insert Node
        node.next = curr
        prev.next = node

        return head


if __name__ == "__main__":
    l1 = list_to_link([3, 4, 6, 1])
    sol = Solution().insert(l1, 2)
    print_ll(sol)
