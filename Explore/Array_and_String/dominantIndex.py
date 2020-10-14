class Solution:
    def dominantIndex(self, nums):
        max_i = nums.index(max(nums))
        max_num = nums[max_i]

        for i in range(len(nums)):
            if i == max_i:
                continue

            if not max_num >= 2 * nums[i]:
                return -1

        return max_i

#nums = [3,6,1,0]
nums = list(map(int, input().split()))
s = Solution()
print(s.dominantIndex(nums))
