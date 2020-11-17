# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        fast = slow = head
        rev_head = None

        # find the middle of the Linked List (slow will be the middle)
        while fast and fast.next:
            fast = fast.next.next
            rev_head, rev_head.next, slow = slow, rev_head, slow.next

        # if fast exists, the rest half start from slow.next
        if fast:
            slow = slow.next

        # compare the rest half (start from slow) and the reversed half
        while rev_head and slow.val == rev_head.val:
            slow, rev_head = slow.next, rev_head.next

        return not rev_head
