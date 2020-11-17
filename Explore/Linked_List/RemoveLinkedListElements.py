# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def removeElements_recursive(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements_recursive(head.next, val)
        return head.next if head.val == val else head

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        dummy_head = ListNode(-1, head)
        node = dummy_head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummy_head.next
