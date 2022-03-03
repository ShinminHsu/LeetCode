from LinkedList import LinkedList, LinkedListNode

def findKLast(l: LinkedList, k: int) -> LinkedListNode:

    slow = fast = l.head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


class Solution:
    def findKLast_recursion(self, head: LinkedListNode, k: int) -> int:
        self.index = 0

        if not head:
            return None

        node = self.findKLast_xrecursion(head.next, k)
        self.index += 1

        if self.index == k:
            return head

        return node

values = [1,2,2,1,3,5,7,2,2,1]
k = 3
answer = [2]
l = LinkedList()
l.add_multiple(values)

s = Solution()
print(s.findKLast_recursion(l.head, k))

