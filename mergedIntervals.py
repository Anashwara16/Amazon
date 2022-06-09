
# 56. Merge Intervals


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()

        mergedList = []

        for interval in intervals:

            if not mergedList or mergedList[-1][1] < interval[0]:
                mergedList.append(interval)

            else:
                mergedList[-1][1] = max(mergedList[-1][1], interval[1])

        return mergedList


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    objectNums = Solution()
    print(objectNums.merge(intervals))
