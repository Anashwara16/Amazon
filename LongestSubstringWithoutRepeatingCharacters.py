
# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        left = result = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, (right - left + 1))

        return result


if __name__ == "__main__":
    s = "abcabcbb"
    objectNums = Solution()
    print(objectNums.lengthOfLongestSubstring(s))
