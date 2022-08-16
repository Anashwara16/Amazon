
# 32. Longest Valid Parentheses


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = right = maxLength = 0

        for c in s:

            if c == "(":
                left += 1
            elif c == ")":
                right += 1

            if left == right:
                maxLength = max(maxLength, (2*right))

            elif right >= left:
                left = right = 0

        left = right = 0

        for c in reversed(s):

            if c == "(":
                left += 1
            elif c == ")":
                right += 1

            if left == right:
                maxLength = max(maxLength, (2*left))

            elif left >= right:
                left = right = 0

        return maxLength


if __name__ == "__main__":
    s = ")()())"
    objectNums = Solution()
    print(objectNums.longestValidParentheses(s))
