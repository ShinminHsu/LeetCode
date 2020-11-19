# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1.val >= l2.val:
            head = node = l1
            l1 = l1.next
        else:
            head = node = l2
            l2 = l2.next


        while l1 and l2:
            while l1.val <= l2.val:
                node.next = l1
                node, l1 = node.next, l1.next

            while l2.val <= l1.val:
                node.next = l2
                node, l2 = node.next, l2.next

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return head

            