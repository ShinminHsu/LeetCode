from LinkedList import LinkedList, LinkedListNode

def deleteMiddleNode(l: LinkedList) -> LinkedList:

    head = l.head

    # make sure it's not the only node or tail
    if not head or not head.next or not head.next.next:
        return head

    head.next = head.next.next

    return l

def deleteMiddleNode(node: LinkedListNode):

    if not node or not node.next:
        return

    node = node.next.value
    node.next = node.next.next

    return

values = [1,2,2,1]
l = LinkedList()
l.add_multiple(values)

print(deleteMiddleNode(l))