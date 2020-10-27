from queue import Queue

class Solution:
    def openLock(self, deadends, target):

        code = "0000"
        self.visited = []
        self.waiting = Queue()
        self.waiting.put(code)

        self.deadends = deadends
        self.target = target
        self.counter = 0

        count = 0
        while count < 10:
        # while self.waiting:
            count+=1
            code = self.waiting.get()
            if code == self.target:
                break
            self.checkCode(code)

        print(self.counter)

    def checkCode(self, code):
        self.counter += 1

        for i, c in enumerate(code):
            up = code[:i] + self.rotateForward(c) + code[i+1:]
            down = code[:i] + self.rotateBackward(c) + code[i+1:]
            print(up, down)

            for new_code in up, down:
                if new_code not in self.deadends and new_code not in self.visited:
                    self.visited.append(new_code)
                    self.waiting.put(new_code)
                    #return self.checkCode(new_code)


    def rotateForward(self, num):
        return str((int(num) + 1) % 10)

    def rotateBackward(self, num):
        return str((int(num) - 1) % 10)

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
s = Solution()
s.openLock(deadends, target)
