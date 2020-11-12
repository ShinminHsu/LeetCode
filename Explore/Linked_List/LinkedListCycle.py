# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or head.next is None:
            return False

        fast = head.next.next
        slow = head

        while (fast is not None) and (fast.next is not None) and (slow is not None):
            if fast.val == slow.val:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
