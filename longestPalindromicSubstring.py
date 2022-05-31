
# 5. Longest Palindromic Substring


class Solution:

    def longestPalindrome(self, s: str) -> str:

        result = ""

        for i in range(len(s)):

            # this is for odd length palindrome
            print("Values provided for word1: ", i, i)
            word1 = self.checkPalindrome(s, i, i)
            print("Word 1: ", word1)

            # this is for even length palindrome
            print("Values provided for word2: ", i, i+1)
            word2 = self.checkPalindrome(s, i, i+1)
            print("Word 2: ", word2)

            longerWord = word1 if len(word1) > len(word2) else word2
            print("Longer Word: ", longerWord)

            result = longerWord if len(longerWord) > len(result) else result
            print("Result: ", result)

        return result

    def checkPalindrome(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            print("Characters are equal")
            l -= 1
            r += 1

        print("Start:", l+1)
        print("End", r)
        print("Sliced string before returning ==>", s[l+1:r])
        return s[l+1:r]


if __name__ == "__main__":
    s = "babad"
    objectNums = Solution()
    print(objectNums.longestPalindrome(s))
