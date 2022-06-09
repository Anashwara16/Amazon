
# 253. Meeting Rooms II


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:

        if not intervals:
            return 0

        startTimings = sorted([i[0] for i in intervals])
        endTimings = sorted([i[1] for i in intervals])

        usedRooms = 0
        numberOfIntervals = len(intervals)
        startPointer = endPointer = 0

        while startPointer < numberOfIntervals:

            if startTimings[startPointer] >= endTimings[endPointer]:
                endPointer += 1
                usedRooms -= 1

            usedRooms += 1
            startPointer += 1

        return usedRooms


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    objectNums = Solution()
    print(objectNums.minMeetingRooms(intervals))
