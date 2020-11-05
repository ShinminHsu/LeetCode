from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.put(x)
        for _ in range(self._queue.qsize() - 1):
            self._queue.put(self._queue.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._queue.get()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self._queue.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if self._queue.qsize() == 0 else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
