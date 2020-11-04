class Solution:
    def openLock(self, deadends, target):

        self.deadends = set(deadends)
        if target in deadends:
            return -1

        waiting = ["0000"]
        depth = 0

        while waiting:
            size = len(waiting)
            for _ in range(size):
                code = waiting.pop(0)

                if code in self.deadends:
                    continue
                if code == target:
                    return depth
                for new_code in self.checkCode(code):
                    waiting.append(new_code)
            depth += 1
        return -1

    def checkCode(self, code):
        for i, c in enumerate(code):
            for n in [-1, 1]:
                new_code = code[:i] + self.rotate(c, n) + code[i + 1:]
                self.deadends.add(new_code)
                if new_code not in self.deadends:
                    yield new_code

    def rotate(self, c, n):
        return str((int(c) + n) % 10)


deadends = ["0000"]
target = "8888"
s = Solution()
print(s.openLock(deadends, target))
