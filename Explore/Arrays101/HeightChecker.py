class Solution:
    def HeightChecker(self, heights):
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1

        return count

heights = [1,2,3,4,5]
s = Solution()
print(s.HeightChecker(heights))