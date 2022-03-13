class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1 and k == 1:
            return 0
        
        convert_table = {'0': '01', '1': '10'}
        parentK = lambda x: (x-1)//2 + 1

        def helper(n, k):
            if n == 1:
                return '0'
            preK = parentK(k)
            return convert_table[helper(n - 1, preK)][k-1]


class Solution2:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        如果 k 是奇數，則和 parent 的數值一樣
        若是偶數，則和 parent 的數值相反
        """

        convert_table = {0: 1, 1: 0}
        parentK = lambda x: (x-1)//2 + 1

        if n == 1 and k == 1:
            return 0

        if k % 2 == 0:
            return convert_table[self.kthGrammar(n-1, parentK(k))]
        else:
            return self.kthGrammar(n-1, parentK(k))
        
        