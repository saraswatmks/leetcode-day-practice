"""
Rotate List
https://leetcode.com/problems/rotate-list/

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""

from utils import ListNode, list_to_link, print_ll

class Solution:
    def rotateRight(self, head: ListNode, k: int):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return head

        # need length of list to normalize k later
        n = 0
        tmp = head
        # last_node = ListNode(-1)
        # last_node.next = tmp

        while tmp.next:
            n += 1
            tmp = tmp.next
        
        # make rotate link, set last node to first
        tmp.next = head
        
        # normalize k
        k = k % n

        # no need to rotate, already rotated
        if k == 0:
            return head
        
        # new tail = (n - k - 1
        # new head = (n - k)
        new_tail = head
        for i in range(n-k-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head


if __name__ == "__main__":
    l1 = list_to_link([1,2,3,4,5])
    sol = Solution().rotateRight(l1, k=25)
    print_ll(sol)