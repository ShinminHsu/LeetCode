class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x

        self.stack.append((x, curMin))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) != 0 else None
        

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) != 0 else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()