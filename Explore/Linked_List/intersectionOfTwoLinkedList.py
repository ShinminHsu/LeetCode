# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        a, b = headA, headB

        # compare a+b and b+a
        # if they meet, a or b is what we are looking for
        # if they don't meet, they will all be None eventually
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
