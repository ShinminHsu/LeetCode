from LinkedList import LinkedList, LinkedListNode

def sum_list(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:

    carry = 0
    res = node = LinkedListNode(0)

    while l1 and l2:

        carry, val = divmod(l1.value + l2.value + carry, 10)
        node.next = LinkedListNode(val)
        node = node.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        carry, val = divmod(l1.value + carry, 10)
        node.next = LinkedListNode(val)
        node = node.next
        l1 = l1.next

    while l2:
        carry, val = divmod(l2.value + carry, 10)
        node.next = LinkedListNode(val)
        node = node.next
        l2 = l2.next

    if carry:
        node.next = LinkedListNode(carry)

    return res.next


def sum_list(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:

    def helper(node1, node2, carry):
        if not node1 and not node2 and not carry:
            return None

        val = carry
        
        if node1:
            val += node1.value
        if node2:
            val += node2.value

        res = LinkedListNode(val // 10)

        if not node1 or not node2:
            res.next = helper(node1.next, node2.next, val % 10)

        return res

    return helper(l1.head, l2.head, 0)
        


def sum_list_followup(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:

    """The digits are stored in forward order: 6->1->7 + 2->9->5 = 9->1->2"""
    """Create the node until move to the next element, store 6 + 2 (= pre_val) first, and then compute 1+9 (get value = 0 and carry = 1), and then create a node"""
    # what if pre_val = 9 and carry = 1?

    res = node = LinkedListNode(0)
    pre_val = 0

    l1_list = list()
    l2_list = list()

    while l1:
        l1_list.append(l1.value)
    while l2:
        l2_list.append(l2.value)


    while l1 and l2:
        carry, val = divmod(l1.value + l2.value, 10)

    return

l1 = LinkedList([9,7,8,1])  #1879
l2 = LinkedList([6,8,5])  #586

print(l1, l2)

res = sum_list(l1.head, l2.head)

while res:
    print(res.value, end='->')
    res = res.next