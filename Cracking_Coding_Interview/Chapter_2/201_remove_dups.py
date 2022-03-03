from cProfile import run
from LinkedList import LinkedList, LinkedListNode
from collections import defaultdict

def removeDups_CtCI(l: LinkedList) -> LinkedList:
    """
    CTCI needs to keep all the elements and just remove other duplicates
    Example. [1,1,2,2] -> [1,2]
    Time complexity: O(n)
    Space complexity: O(n)
    """

    if not l.head:
        return

    node = l.head
    seen = set([node.value])

    while node.next:
        if node.next.value in seen:
            node.next = node.next.next
        else:
            seen.add(node.next.value)
            node = node.next

    return l

def removeDups_CtCI_followup(l: LinkedList) -> LinkedList:
    """
    without using buffer, use two pointers instead
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    if not l.head:
        return

    current = l.head

    while current.next:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next  # skip the next one
            else:
                runner = runner.next

        current = current.next

    return l
    

def removeDups_LeetCode(l: LinkedList) -> LinkedListNode:

    """
    LeetCode requires us to remove ALL the duplicates
    Example. [1,1,2,2] -> []
    """

    if not l.head:
        return

    hash_map = defaultdict(lambda: 0)
    
    dummy_head = prev = LinkedListNode(0)

    node = l.head
    # First: go through the linked list once to check what values are in the linked list
    while node:
        hash_map[node.value] += 1
        node = node.next

    node = l.head
    # Second: remove duplicate
    while node:
        if hash_map[node.value] == 1:
            print(node.value)
            prev.next = node
            prev = node

        node = node.next

    return dummy_head.next

values = [1,2,2,1,3,5,7,2,2,1]
answer = [3,5,7]
l = LinkedList()
l.add_multiple(values)

print(l)

res = removeDups_CtCI_followup(l)
print(res)
# values = [1,2,2,1]
# answer = []
