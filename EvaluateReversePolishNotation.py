
# 150. Evaluate Reverse Polish Notation


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
                continue

            number2 = stack.pop()
            number1 = stack.pop()
            result = 0

            if token == "+":
                result = number1 + number2

            elif token == "-":
                result = number1 - number2

            elif token == "*":
                result = number1 * number2

            else:
                result = int(number1 / number2)

            stack.append(result)

        return stack.pop()


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    objectNums = Solution()
    print(objectNums.evalRPN(tokens))
