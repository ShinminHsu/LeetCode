class Solution:
    def sortArrayByParity(self, A):
        if not A:
            return A

        even_index, odd_index = -1, -1

        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_index += 1
                A[i], A[even_index] = A[even_index], A[i]
            else:
                odd_index += 1

        return A

A = list(map(int, input().split()))
s = Solution()
s.sortArrayByParity(A)
