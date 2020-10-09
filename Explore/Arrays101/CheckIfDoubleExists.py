class Solution:
    def checkIfExist(self, arr):
        if not arr or len(arr) == 1:
            return False

        hashtable = {}
        zero_count = 0

        for num in arr:
            hashtable[2 * num] = True

        for num in arr:
            if num in hashtable and num != 0:
                return True
            elif num in hashtable and num == 0:
                if zero_count == 1:  # find another zero
                    return True
                else:
                    zero_count += 1

        return False

arr = [0,1]
s = Solution()
print(s.checkIfExist(arr))
