# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        initial_head = head

        while initial_head.next:
            # the new head is always next to the initial head
            # put the new head before the old head
            # since the new head is removed, connect the element next to the new head to the initial head
            head, head.next, initial_head.next = initial_head.next, head, initial_head.next.next

        return head


