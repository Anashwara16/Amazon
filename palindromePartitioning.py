
# 131. Palindrome Partitioning


class Solution:
    def partition(self, s: str) -> list[list[str]]:

        res = []
        part = []

        def dfs(i):

            if i >= len(s):
                res.append(part.copy())
                print("Result: ", res)
                return

            for j in range(i, len(s)):

                print("*** New Iteration *** -- i & j -- ", i, j)

                if self.isPalindrome(s, i, j):
                    print("Is a palindrome!")
                    print("String to be added: ", s[i:j+1])
                    part.append(s[i:j+1])
                    print("Part after adding new palindrome string: ", part)
                    dfs(j+1)
                    print("Part before popping: ", part)
                    part.pop()
                    print("Part after popping: ", part)

        dfs(0)

        return res

    def isPalindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    s = "aab"
    objectNums = Solution()
    print(objectNums.partition(s))
