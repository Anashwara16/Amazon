
# 387. First Unique Character in a String

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)

        for index, character in enumerate(s):
            if count[character] == 1:
                return index

        return -1


if __name__ == "__main__":
    s = "loveleetcode"
    objectNums = Solution()
    print(objectNums.firstUniqChar(s))
