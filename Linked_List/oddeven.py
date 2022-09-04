"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

https://leetcode.com/problems/odd-even-linked-list/

"""

from utils import ListNode, list_to_link, print_ll

class Solution:
    def oddEven1(self, head: ListNode):
        """
        Idea is to create two ll, one for even another one for odd.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        odd = head
        even = head.next
        evenHead =head.next
        
        # we use even since it'll go null before odd nodes.
        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = evenHead
        return head


if __name__ == "__main__":
    ll = [1,5,7,3,4,2,8]
    ll = list_to_link(ll)
    sol = Solution().oddEven1(ll)
    print_ll(sol)