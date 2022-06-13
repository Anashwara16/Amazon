
# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 0
        count = {}
        l = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, (r-l+1))

        return result


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    objectNums = Solution()
    print(objectNums.characterReplacement(s, k))
