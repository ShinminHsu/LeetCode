class Node:
    def __init__(self, val=None, nxt=None, pre=None):
        """
        Initialize a new node.
        """
        self.val = val
        self.next = nxt
        self.pre = pre


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        nthNode = self.getNode(index)

        if not nthNode:
            return -1

        return nthNode.val
        

    def getNode(self, index: int) -> Node:
        """
        Get the the index-th node in the linked list. If the index is invalid, return None.
        """

        if index < 0 or index >= self.size:
            return None

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)

        if self.head:
            self.head.pre, self.head, node.next = node, node, self.head

        else:
            self.head = node

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        if self.head is None:
            self.head = Node(val)

        else:
            tail = self.getNode(self.size - 1)
            tail.next = Node(val, None, tail)

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.size:
            return
        
        if index == self.size:
            self.addAtTail(val)

        elif index == 0:
            self.addAtHead(val)

        else:
            nxt = self.getNode(index)
            pre = nxt.pre

            node = Node(val, nxt, pre)
            pre.next = node
            nxt.pre = node

            self.size += 1  # addAtTail and addAtHead have already increased the size


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index >= self.size:
            return

        elif index == 0:
            self.head = self.head.next

        elif index == self.size - 1:
            target = self.getNode(index)
            target.pre.next = None

        else:
            target = self.getNode(index)
            target.pre.next, target.next.pre = target.next, target.pre

        self.size -= 1

    def print_node(self):
        node = self.head
        while node:
            print(node.val, end=',')
            node = node.next

        print('\n')


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

obj.addAtHead(2)
obj.print_node()

obj.deleteAtIndex(1)
obj.print_node()

obj.addAtHead(2)
obj.print_node()

obj.addAtHead(7)
obj.print_node()

obj.addAtHead(3)
obj.print_node()

obj.addAtHead(2)
obj.print_node()

obj.addAtHead(5)
obj.print_node()

obj.addAtTail(5)
obj.print_node()

print(obj.get(5))

obj.deleteAtIndex(6)
obj.print_node()

obj.deleteAtIndex(4)
obj.print_node()

obj.deleteAtIndex(0)
obj.print_node()