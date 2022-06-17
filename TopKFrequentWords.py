
# 692. Top K Frequent Words

import collections
import heapq


class heapItem:
    def __init__(self, count, word):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word

        return self.count < other.count


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        wordCount = collections.Counter(words)

        wordHeap = []

        for word, count in wordCount.items():

            heapq.heappush(wordHeap, heapItem(count, word))

            if len(wordHeap) > k:
                heapq.heappop(wordHeap)

        result = []

        while wordHeap:
            result.append(heapq.heappop(wordHeap).word)

        result.reverse()

        return result


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    objectNums = Solution()
    print(objectNums.topKFrequent(words, k))
