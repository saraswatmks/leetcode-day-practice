"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

https://leetcode.com/problems/palindrome-linked-list/

"""

from utils import print_ll, ListNode, list_to_link
from collections import deque
class Solution:
    def isPalindromeOne(self, head: ListNode):
        """
            Done in three steps:
            1. Find the mid of the list.
            2. Reverse the second half of the list
            3. Compare the first and second half if palindrome.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        slow = fast = head
        # find mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # compare the first and second half nodes
        # prev contain reversed second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    def isPalindromeTwo(self, head: ListNode):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        queue = deque([])
        cur = head
        while cur:
            queue.append(cur)
            cur = cur.next
        while len(queue) >= 2:
            if queue.popleft().val != queue.pop().val:
                return False
        return True



if __name__ == "__main__":
    ll = [1,2,2,1]
    ll = list_to_link(ll)
    sol = Solution().isPalindromeOne(ll)
    print(sol)