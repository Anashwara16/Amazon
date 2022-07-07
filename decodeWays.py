
# 91. Decode Ways


class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [1]*(len(s)+1)

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                dp[i] = 0

            else:
                dp[i] = dp[i+1]

            if (i+1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in ["0", "1", "2", "3", "4", "5", "6"]):
                dp[i] += dp[i+2]

        return dp[0]


if __name__ == "__main__":
    s = "226"
    objectNums = Solution()
    print(objectNums.numDecodings(s))
