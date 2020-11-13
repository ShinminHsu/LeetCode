class Node:
    def __init__(self, val=None, nxt=None):
        """
        Initialize a new node.
        """
        self.val = val
        self.next = nxt


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

        if nthNode is None:
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
        node = Node(val, self.head)
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
            tail.next = Node(val)

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
            pre = self.getNode(index - 1)
            nxt = pre.next

            pre.next = Node(val, nxt)

            self.size += 1  # addAtTail and addAtHead have already increased the size

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next

        else:
            pre = self.getNode(index - 1)
            pre.next = pre.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(0)
print(obj.head.val, obj.size)
obj.addAtIndex(1, 4)
obj.addAtTail(8)
print(obj.head.val, obj.head.next.val, obj.size)

obj.addAtHead(5)
obj.addAtIndex(4, 3)
obj.addAtTail(0)
print(obj.head.val, obj.head.next.val, obj.head.next.next.val, obj.head.next.next.next.val, obj.size)

obj.addAtTail(5)
obj.addAtIndex(6, 3)
# print(obj.head.val, obj.head.next.val, obj.size)

obj.deleteAtIndex(7)
# print(obj.head.val, obj.head.next.val, obj.size)

obj.deleteAtIndex(5)
# print(obj.head.val, obj.head.next.val, obj.size)

obj.addAtTail(4)
# print(obj.head.val, obj.head.next.val, obj.size)