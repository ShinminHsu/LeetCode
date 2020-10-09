class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        j = n + arr.count(0) - 1
        for i in range(n-1, -1, -1):
            
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            j -= 1
                
        print(arr)
        

s = Solution()
s.duplicateZeros([1,0,2,3,0,4,0,5])