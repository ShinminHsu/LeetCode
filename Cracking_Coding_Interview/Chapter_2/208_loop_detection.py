from LinkedList import LinkedList, LinkedListNode

def loopDetection(l: LinkedList) -> LinkedListNode:

    seen = set()
    node = l.head

    while node not in seen:
        seen.add(node)
        node = node.next

    return node


def loopDetection_2(l: LinkedList) -> LinkedListNode:
    # use fase and slow pointers

    fast = slow = l.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None
    
    head = l.head
    while slow != head:
        slow = slow.next
        head = head.next
    return head