"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

https://leetcode.com/problems/add-two-numbers/
"""

from utils import print_ll, list_to_link, ListNode

class Solution:
    def addNumbers(self, l1: ListNode, l2: ListNode):
        """
        Time Complexity: O(max(M, N))
        Space Complexity: O(1)
        """
        
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry = carry // 10
        
        return dummy.next

if __name__ == "__main__":
    l1 = list_to_link([2,4,3])
    l2 = list_to_link([5,6,4])
    sol = Solution().addNumbers(l1, l2)
    print_ll(sol)
