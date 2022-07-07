
# 395. Longest Substring with At Least K Repeating Characters

from collections import Counter, defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        n = len(s)
        maxLen = 0
        maxNums = len(Counter(s))

        for num in range(1, maxNums+1):

            hashmap = defaultdict(int)
            l = 0

            for r in range(n):

                hashmap[s[r]] += 1

                print("Length of hashmap: ", len(hashmap))

                while len(hashmap) > num:

                    print("Length of hashmap greater than number")

                    hashmap[s[l]] -= 1

                    if hashmap[s[l]] == 0:
                        del hashmap[s[l]]

                    l += 1

                for key in hashmap:

                    if hashmap[key] >= k:
                        flag = 1

                    else:
                        flag = 0
                        break

                if flag == 1:
                    maxLen = max(maxLen, r - l + 1)

        return maxLen


if __name__ == "__main__":
    s = "aaabb"
    k = 3
    objectNums = Solution()
    print(objectNums.longestSubstring(s, k))
