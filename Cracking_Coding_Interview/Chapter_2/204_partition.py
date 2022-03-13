from LinkedList import LinkedList, LinkedListNode


def partition(l: LinkedList, p: int) -> LinkedList:
    
    small_head = small = LinkedListNode(0)
    large_head = large = LinkedListNode(0)
    equal_head = equal = LinkedListNode(0)

    node = l.head

    while node:
        if node.value < p:
            small.next = node
            small = small.next

        elif node.value > p:
            large.next = node
            large = large.next
        
        else:
            equal.next = node
            equal = equal.next

        node = node.next

    # concatnate three linked lists
    small.next = equal_head.next
    equal.next = large_head.next
    large.next = None

    return small_head.next

def partition2(l: LinkedList, p: int) -> LinkedList:

    node = l.head
    head = node
    tail = node

    while node:
        if node.value < p:
            node.next = head
            head = node

        else:
            tail.next = node
            tail = node

        node = node.next

    tail.next = None
    return head

values = [3,5,8,5,10,2,1]
p = 5
l = LinkedList()
l.add_multiple(values)

res = partition(l, p)

while res:
    print(res.value, end='->')
    res = res.next
