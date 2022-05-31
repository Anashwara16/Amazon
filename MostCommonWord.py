
# 819. Most Common Word


from collections import defaultdict
from ast import operator
from operator import itemgetter


class Solution:

    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        normalizedStr = ''.join(
            [c.lower() if c.isalnum() else ' ' for c in paragraph])

        words = normalizedStr.split()

        wordCount = defaultdict(int)
        bannedWords = set(banned)

        for word in words:
            if word not in bannedWords:
                wordCount[word] += 1

        return max(wordCount.items(), key=itemgetter(1))[0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    objectNums = Solution()
    print(objectNums.mostCommonWord(paragraph, banned))
