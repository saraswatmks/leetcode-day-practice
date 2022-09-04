"""Contains utils functions for linked list questions."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_link(lst) -> ListNode:
    """Takes a Python list and returns a Link with the same elements."""
    if len(lst) == 1:
        return ListNode(lst[0])
    return ListNode(lst[0], list_to_link(lst[1:]))  # <<<< RECURSIVE

def print_ll(head) -> None:
    """Takes the head of a linked list and prints it"""
    while head:
        print(head.val, end='->')
        head = head.next
    print("\n")