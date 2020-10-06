class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        
        if n == 0:
            return

        i = m - 1
        j = n - 1

        while i + j + 1 >= 0:
            if i == -1:  # when all the elements in nums1 were moved, then only need to move elements in nums2
                nums1[:j+1] = nums2[:j+1]
                break

            if j == -1: # when all the elements in nums2 were moved, then no need to move elements in nums1
                break

            if nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[i+j+1] = nums2[j]
                j -= 1
            elif nums1[i] == nums2[j]:
                nums1[i+j+1] = nums1[i]
                nums1[i+j] = nums2[j]
                i -= 1
                j -= 1

nums1 = [2, 0, 0]
nums2 = [1, 1]
m = 1
n = 2

s = Solution()
s.merge(nums1, m, nums2, n)

print(nums1)