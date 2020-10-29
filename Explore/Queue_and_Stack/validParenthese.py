class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairParentheses = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        for p in s:
            if p in pairParentheses.values():  # ["(", "[", "{"]
                stack.append(p)

            elif p in pairParentheses.keys():  # [")", "]", "}"]

                # cannot find its pairs
                if len(stack) == 0:
                    return False

                top_stack = stack.pop()

                if top_stack != pairParentheses[p]:
                    return False

        return True if len(stack) == 0 else False