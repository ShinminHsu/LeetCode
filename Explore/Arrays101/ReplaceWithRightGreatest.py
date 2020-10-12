class Solution:
    def replaceElements(self, arr):
        if not arr:
            return arr
        L = len(arr)
        arr[-1], right_max = -1, arr[-1]

        for i in range(L-2, -1, -1):
            if arr[i] > right_max:
                arr[i], right_max = right_max, arr[i]
            else:
                arr[i] = right_max

        print(arr)

arr = list(map(int, input().split()))
s = Solution()
s.replaceElements(arr)
