"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""
from utils import list_to_link, ListNode, print_ll

class Solution:
    def removeNthNode(self, head: ListNode, n: int):

        """
        This solution uses only one pass.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        fast = slow = head
        for i in range(n):
            fast = fast.next
        
        # delete the head itself, return null
        if not fast:
            return head.next
        
        # we must stop before reaching null
        while fast.next:
            fast = fast.next
            slow = slow.next
        # delete the node
        slow.next = slow.next.next
        return head


    def removeNthNodeTwo(self, head: ListNode, n: int):
        """
        This is a two pass solution. 

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        ptr = head
        length = 0

        # calculate length
        while ptr:
            ptr = ptr.next
            length += 1
        
        if length == n:
            return head.next
        
        # reset the pointer to head
        ptr = head

        for i in range(1, length - n):
            ptr = ptr.next
        
        # remove the node
        ptr.next = ptr.next.next
        return head

if __name__  == "__main__":
    l = [1,2,3,4,5,6]
    n = 2
    ll = list_to_link(l)
    sol = Solution().removeNthNode(ll, n)
    print_ll(sol)
    sol = Solution().removeNthNodeTwo(ll, n)
    print_ll(sol)



