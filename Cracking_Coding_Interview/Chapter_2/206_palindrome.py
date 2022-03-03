import unittest
from LinkedList import LinkedList, LinkedListNode

def palindrome(l: LinkedList) -> bool:

    """Check if a linked list is a palindrome"""

    if not l:
        return False

    list = []
    node = l.head
    while node:
        list.append(node.value)
        node = node.next

    left ,right = 0, len(list) - 1

    while left <= right:
        if list[left] != list[right]:
            return False

        left += 1
        right -= 1


    return True

class Solution2:

    def palindrome(self, l: LinkedList) -> bool:

        """
        Check if a linked list is a palindrome: reverse the linked list
        """

        if not l:
            return False

        l1 = l.head
        l2 = self.reverseLinkedList(l.head)

        return self.isEqual(l1, l2)

    def reverseLinkedList(self, node: LinkedListNode) -> LinkedListNode:
        prev = None
        cur = node

        # reverse the linked list
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        return prev

    
    def isEqual(self, l1: LinkedListNode, l2: LinkedListNode) -> bool:

        while l1 and l2:
            if l1.value != l2.value:
                return False
            l1 = l1.next
            l2 = l2.next

        return True

class Solution3:
    """Use a stack"""
    def palindrome(self, l: LinkedList):

        """
        1  2  3  2  1
                    f fn
              s

        stack: [1, 2]
        """

        stack = []
        # length = self.get_length(l)  # we can use fast and slow instead
    
        fast = slow = l.head

        while fast and fast.next:
            stack.append(slow.value)
            fast = fast.next.next
            slow = slow.next

        # When the length is odd, since fast.next is None so it'll break the loop, but slow will be in the middle
        # We need to skip the middle one by checking if fast is None
        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if slow.value != top:
                return False
            slow = slow.next

        return True


    def get_length(self, l: LinkedList) -> int:

        count = 0
        node = l.head
        while node:
            count += 1
            node = node.next
        
        return count


class Test(unittest.TestCase):
    data = [
        (LinkedList([9,7,7,9]), True),
        (LinkedList([9,7,1,7,9]), True),
        (LinkedList([9,9]), True),
        (LinkedList([9]), True),
        (LinkedList([9,7]), False),
        (LinkedList([9,9,7,5]), False)
    ]

    def test_palindrome(self):
        s = Solution3()
        for test_ll, ans in self.data:
            res = s.palindrome(test_ll)
            self.assertEqual(ans, res)

if __name__ == '__main__':
    unittest.main()

    # ll = LinkedList([9,7,7,9])
    # print(palindrome2(ll))
