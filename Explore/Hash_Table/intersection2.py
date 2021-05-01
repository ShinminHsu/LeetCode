class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums_hash = {}
        result = []
        
        for i in nums1:
            if i not in nums_hash:
                nums_hash[i] = 1
            else:
                nums_hash[i] += 1

        for j in nums2:
            if j in nums_hash and nums_hash[j] > 0:
                result.append(j)
                nums_hash[i] -= 1

        return result
