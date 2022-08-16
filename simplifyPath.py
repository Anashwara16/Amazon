
# 71. Simplify Path


from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)
        print(count)
        maxHeap = [[-cnt, ch] for ch, cnt in count.items()]
        print(maxHeap)
        prev = None
        res = ""

        while maxHeap or prev:

            if prev and not maxHeap:
                return ""

            cnt, ch = heapq.heappop(maxHeap)
            print(cnt, ch)
            res += ch
            print("Res", res)
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                heapq.heapify(maxHeap)
                prev = None

            if cnt != 0:
                prev = [cnt, ch]

        return res


if __name__ == "__main__":
    s = "aab"
    objectNums = Solution()
    print(objectNums.reorganizeString(s))
