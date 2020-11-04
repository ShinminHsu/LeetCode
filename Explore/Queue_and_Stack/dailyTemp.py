class Solution:
    def dailyTemperatures(self, T):

        days = [0] * len(T)
        stack = [(T[0], 0)]

        for i, t in enumerate(T[1:]):

            if not stack:
                stack.append((t, i + 1))
                continue

            while stack and (t > stack[-1][0]):
                top, index = stack.pop()
                days[index] = i + 1 - index
                
            stack.append((t, i + 1))

        return days


T = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
print(s.dailyTemperatures(T))