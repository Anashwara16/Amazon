
# 22. Generate Parentheses


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        result = []

        def backtrack(openCount, closedCount):

            if openCount == closedCount == n:
                result.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount+1, closedCount)
                stack.pop()

            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount+1)
                stack.pop()

        backtrack(0, 0)

        return result


if __name__ == "__main__":
    n = 3
    objectNums = Solution()
    print(objectNums.generateParenthesis(n))
