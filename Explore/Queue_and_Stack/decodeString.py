class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        stack, substring, curNum = [], "", 0

        for c in s:
            if c.isdigit():
                # put previous substring onto stack if it is not empty
                curNum = 10 * curNum + int(c)
                if substring:
                    stack.append(substring)
                    substring = ""

            elif c == "]":
                top = stack.pop()
                if isinstance(top, int):
                    output += substring * top  # pop curNum stored in the "[" step
                    substring = ""
                else:
                    output = (top + output) * stack.pop()

            elif c == "[":
                # put the previous number onto the stack and set curNum as zero
                stack.append(curNum)
                curNum = 0

            else:
                substring += c

        if stack:
            output = stack.pop() + output

        return output + substring

string = "3[2[cd]xyz]"
solution = Solution()
print(solution.decodeString(string))
