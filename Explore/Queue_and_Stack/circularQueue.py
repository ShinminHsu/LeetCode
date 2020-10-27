class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.capacity = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :param value: int
        :return bool
        """
        if self.isEmpty():
            self.head += 1
        elif self.isFull():
            return False

        if self.tail == self.capacity - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = value

        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.head == self.capacity - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.head] if self.head != -1 else -1


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.tail] if self.tail != -1 else -1


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if ((self.head == -1) and (self.tail == -1)) else False


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        if ((self.tail - self.head) == self.capacity - 1) or (self.head - self.tail) == 1:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
k = 2
obj = MyCircularQueue(k)
print(obj.enQueue(4))
print(obj.Rear())
print(obj.enQueue(9))
print(obj.deQueue())
print(obj.Front())

print(obj.deQueue())
print(obj.deQueue())
print(obj.isEmpty())
print(obj.deQueue())
print(obj.enQueue(6))

print(obj.enQueue(4))
