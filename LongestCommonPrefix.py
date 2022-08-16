
# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]


if __name__ == "__main__":
    strs1 = ["dog", "racecar", "car"]
    strs2 = ["flower", "flow", "flight"]
    objectNums = Solution()
    print(objectNums.longestCommonPrefix(strs1))
    print(objectNums.longestCommonPrefix(strs2))
