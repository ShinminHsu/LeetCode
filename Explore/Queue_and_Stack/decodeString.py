import unittest

class Solution:
    def decodeString(self, s: str) -> str:
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
                    substring = substring * top  # pop curNum stored in the "[" step
                else:
                    substring = top + substring

                stack.append(substring)  # put the processed substring onto the top
                substring = ""
                print(stack)

            elif c == "[":
                # put the previous number onto the stack and set curNum as zero
                stack.append(curNum)
                curNum = 0

            else:
                substring += c

        if substring:
            stack.append(substring)

        print(stack)
        output = ""
        while stack:
            top = stack.pop()

            if isinstance(top, int):
                curNum = top
                output = curNum * output
            else:
                output = top + output

        return output

class SolutionTestCase(unittest.TestCase):
    def testCase(self):

        stringList = ["3[a]2[bc]", "3[a2[c]]",  "2[abc]3[cd]ef" , "abc3[cd]xyz", "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"]
        answerList = ["aaabcbc",   "accaccacc", "abcabccdcdcdef", "abccdcdcdxyz", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"]

        sol = Solution()

        for s, a in zip(stringList, answerList):
            result = sol.decodeString(s)
            self.assertEqual(result, a) 




string = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
solution = Solution()
print(solution.decodeString(string))
