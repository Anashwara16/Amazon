
# 1094. Car Pooling

import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:

        trips.sort(key=lambda t: t[1])

        minHeap = []
        currentPassengers = 0

        for t in trips:

            numberOfPassengers, start, end = t

            while minHeap and minHeap[0][0] <= start:
                currentPassengers -= minHeap[0][1]
                heapq.heappop(minHeap)

            currentPassengers += numberOfPassengers

            if currentPassengers > capacity:
                return False

            heapq.heappush(minHeap, [end, numberOfPassengers])

        return True


if __name__ == "__main__":
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    objectNums = Solution()
    print(objectNums.carPooling(trips, capacity))
