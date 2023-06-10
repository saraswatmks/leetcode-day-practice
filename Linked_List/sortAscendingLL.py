"""
Given the head of a LL, sort it in ascending order.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

from ast import List

from utils import ListNode, list_to_link, print_ll


class Solution:
    def solutionOne(self, head):
        # base case
        if not head or not head.next:
            return head

        # split the list in two halves
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # get the mid node
        mid = slow.next
        slow.next = None

        print_ll(head)
        print_ll(mid)
        print("*" * 100)

        # sort of each the half
        left = self.solutionOne(head)
        right = self.solutionOne(mid)

        return self._mergesort(left, right)

    def _mergesort(self, l, r):
        # merge the two sorted lists
        if not l or not r:
            return l or r

        dummy = p = ListNode(0)

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next


if __name__ == "__main__":
    ll = list_to_link([4, 2, 1, 3])
    # print_ll(ll)
    s = Solution().solutionOne(ll)
    print_ll(s)
