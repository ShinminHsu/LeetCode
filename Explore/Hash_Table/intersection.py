class Solution1:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

class Solution2:
    def intersection(self, nums1, nums2):
        inter = []
        nums1 = nums1.sort()
        nums2 = nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                inter.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                inter.append(nums2[j])
                j += 1
            else:
                inter.append(nums1[i])
                i += 1
                j += 1
        inter += nums1[i:]
        inter += nums2[j:]

        return inter
