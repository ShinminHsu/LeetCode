# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        node = head

        while node.next:

            if node.next.val == val:
                node.next = node.next.next
                
            node = node.next

        return head