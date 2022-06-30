
# 435. Non-overlapping Intervals


from ast import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort()

        previousEnd = intervals[0][1]
        numberOfOverlaps = 0

        for start, end in intervals[1:]:

            if start >= previousEnd:
                previousEnd = end

            else:
                numberOfOverlaps += 1
                previousEnd = min(end, previousEnd)

        return numberOfOverlaps


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    objectNums = Solution()
    print(objectNums.eraseOverlapIntervals(intervals))
