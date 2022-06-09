
# 973. K Closest Points to Origin


from heapq import heappop
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        minHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        closestPoints = []

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            closestPoints.append([x, y])
            k -= 1

        return closestPoints


if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    k = 1
    objectNums = Solution()
    print(objectNums.kClosest(points, k))
