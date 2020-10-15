class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        :param a: str
        :param b: str
        :return: str
        """
        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a

        na, nb = len(a), len(b)
        output = ''
        carry = False

        # adjust the length of a or b
        if na > nb:
            b = '0' * (na - nb) + b
        elif nb > na:
            a = '0' * (nb - na) + a

        for i in range(len(a)-1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                num = '1' if carry else '0'
                carry = False

            elif a[i] == '1' and b[i] == '1':
                num = '1' if carry else '0'
                carry = True

            else:
                num = '0' if carry else '1'

            output = num + output

        return '1' + output if carry else output


a = input()
b = input()
s = Solution()
print(s.addBinary(a, b))
