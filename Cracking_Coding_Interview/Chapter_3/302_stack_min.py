

class MultiStack:

    def __init__(self, stacksize):

        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [] * (self.numstacks * stacksize)

    def Push(self, item, stacknum) -> None:
        if self.IsFull(stacknum):
            raise Exception(f'Stack {stacknum} is Full')

        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

        # update the self.minvals
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = item
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(item, self.minvals[self.IndexOfTop(stacknum) - 1])
        

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception(f'Stack {stacknum} is Empty')
        
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1

        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception(f'Stack {stacknum} is Empty')
        
        return self.array[self.IndexOfTop(stacknum)]

    def Min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        return stacknum * self.stacksize + self.sizes[stacknum] - 1