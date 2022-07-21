
# Failed Index


class Solution:
    def printFailed(self, maxSize, failedIndex):
        start = failedIndex

        for i in range(maxSize):

            if start < 0:  # and maxSize is full capacity
                start = maxSize - 1
            print(start)
            start -= 1


if __name__ == "__main__":
    maxSize = 10
    failedIndex = 4

    # 432198765
    objectNums = Solution()
    objectNums.printFailed(maxSize, failedIndex)
