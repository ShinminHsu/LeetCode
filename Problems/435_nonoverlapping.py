class Solution:
    def eraseOverlapIntervals(self, intervals):

        pre_e = float("-inf")
        count = 0
        intervals = sorted(intervals, key=lambda item: item[1])

        for nxt_s, nxt_e in intervals:
            
            if nxt_s < pre_e:
                count += 1
            else:
                pre_e = nxt_e

        return count

intervals = [[1,2],[2,3]]
a = Solution()
print(a.eraseOverlapIntervals(intervals))