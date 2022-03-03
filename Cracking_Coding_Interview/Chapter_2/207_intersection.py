# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        len_A, tail_A = self.get_length(headA)
        len_B, tail_B = self.get_length(headB)

        if tail_A != tail_B:
            return None

        # keep the 1st one the longer one
        if len_B > len_A:
            len_B, len_A = len_A, len_B
            headB, headA = headA, headB

        diff = len_A - len_B
        for _ in range(diff):
            headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return headA


    def get_length(self, head: ListNode) -> int:

        if not head:
            return 0

        count = 1
        node = head
        while node.next:
            count += 1
            node = node.next

        return count, node