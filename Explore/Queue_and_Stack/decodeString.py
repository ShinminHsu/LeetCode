import unittest

class Solution:
    def decodeString(self, s: str) -> str:
        stack, curString, curNum = [], "", 0

        for c in s:
            if c.isdigit():
                curNum = 10 * curNum + int(c)

            elif c == "]":
                num, preString = stack.pop()
                curString = preString + num * curString

            elif c == "[":
                # put the previous number onto the stack and set curNum as zero
                stack.append((curNum, curString))
                curNum, curString = 0, ""

            else:
                curString += c

        return curString

class SolutionTestCase(unittest.TestCase):
    def testCase(self):

        stringList = ["3[a]2[bc]", "3[a2[c]]",  "2[abc]3[cd]ef", "abc3[cd]xyz", "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"]
        answerList = ["aaabcbc",   "accaccacc", "abcabccdcdcdef", "abccdcdcdxyz", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"]

        sol = Solution()

        for s, a in zip(stringList, answerList):
            result = sol.decodeString(s)
            self.assertEqual(result, a)


string = "2[ab3[cd]]4[xy]"
solution = Solution()
print(solution.decodeString(string))
