class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = set(["+", "-", "*", "/"])

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(self.operate(token, num1, num2))

            else:
                stack.append(int(token))

        return stack[-1]
                

    def operate(self, token, num1, num2):
        if token == "+":
            return num1 + num2

        elif token == "-":
            return num1 - num2

        elif token == "*":
            return num1 * num2

        elif token == "/":
            return int(num1 / num2)

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(tokens))