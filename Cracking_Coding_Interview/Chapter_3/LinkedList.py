class LinkedListNode:
    def __init__(self, value, nextNode=None, prevNode=None) -> None:
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        values = [str(v) for v in self]
        return ' -> '.join(values)

    def add(self, value):
        if not self.head:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next

        return self.tail

    def add_multiple(self, values):
        for v in values:
            self.add(v)
