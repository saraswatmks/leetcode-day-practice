"""
Remove given elements from the linked list.
https://leetcode.com/problems/remove-linked-list-elements/

"""

# val = 2
# 1 > 2 > 3 > 4
# 1 > 3 > 4

from utils import ListNode, list_to_link, print_ll

class Solution:
    def removeElements(self, head: ListNode, val: int):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

if __name__ == "__main__":
    ll = [7,7,7,7]
    ll = list_to_link(ll)
    sol = Solution().removeElements(ll, 7)
    print_ll(sol)