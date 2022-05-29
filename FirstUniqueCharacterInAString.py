
# 387. First Unique Character in a String

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)

        print(count)

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1


if __name__ == "__main__":
    s = "loveleetcode"
    objectNums = Solution()
    print(objectNums.firstUniqChar(s))
