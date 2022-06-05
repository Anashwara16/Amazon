
# 28. Implement strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        for i in range(len(haystack)+1 - len(needle)):

            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    objectNums = Solution()
    print(objectNums.strStr(haystack, needle))
