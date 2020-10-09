# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        sum = l1.val + l2.val + carry
        carry = sum // 10
        output = ListNode(sum % 10)
        
        if l1.next or l2.next or carry:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            output.next = self.addTwoNumbers(l1, l2, carry)
        
        return output

        

l1 = [2, 4, 4]
l2 = [5, 6, 4]

# output = [7, 0, 9]
        