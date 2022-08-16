
from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        count = Counter(arr)
        minHeap = [[cnt, key] for key, cnt in count.items()]
        heapq.heapify(minHeap)

        while minHeap and k:

            cnt, key = heapq.heappop(minHeap)
            cnt -= 1

            if cnt == 0:
                del count[key]
            else:
                heapq.heappush(minHeap, [cnt, key])

            k -= 1

        return len(minHeap)


if __name__ == "__main__":
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    objectNums = Solution()
    print(objectNums.findLeastNumOfUniqueInts(arr, k))
