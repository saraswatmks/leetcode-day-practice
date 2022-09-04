"""

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. 
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

"""

#TODO: Dont understand fully
class Solution:
    def flatten(self, head):
        """
        Time Complexity: O(2 * N)
        Space Complexity: 
        """
        
        # return if node is None
        if not head:
            return
        
        p = head

        while p:
            # case 1: if no child, proceed
            if not p.child:
                p = p.next
                continue
        
            # case 2: got child, find the tail and link it to p.next
            temp = p.child
            while temp.next:
                temp = temp.next
            
            # connect the tail with p.next, if it is not null
            temp.next = p.next

            if p.next:
                p.next.prev = temp
            # connect p with p.child and remove p.child
            p.next = p.child
            p.child.prev = p
            p.child = None
        return head