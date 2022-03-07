class SetOfStacks:

    def __init__(self, stacksize=3):

        self.numstacks = 1
        self.array = [0]
        self.sizes = 0
        self.stacksize = stacksize


    def Push(self, item) -> None:
        if self.IsFull():
            self.numstacks += 1
        
        self.array.append(item)
        self.sizes += 1


    def Pop(self):
        if self.IsEmpty():
            raise Exception(f'Stack is Empty')
        
        value = self.array[self.sizes - 1]
        self.array[self.sizes - 1] = 0
        self.sizes -= 1

        return value

    def PopAt(self, index):
        """index: start from one"""
        if self.IsEmpty():
            raise Exception(f'Stack is Empty')

        if (self.sizes // self.stacksize + 1) < index:
            raise Exception(f'Index exceeds the size')

        """
        self.sizes 6
        index 1
        """

        return


    def Peek(self):
        if self.IsEmpty():
            raise Exception(f'Stack is Empty')
        
        return self.array[self.sizes - 1]

    def IsEmpty(self):
        return self.sizes == 0

    def IsFull(self):
        return (self.sizes != 0) and (self.sizes % self.stacksize == 0)