
# 7. Reverse Integer

import math


class Solution:
    def reverse(self, x: int) -> int:

        reversedInteger = 0

        MIN = -2147483648
        MAX = 2147483647

        while x:

            digit = int(math.fmod(x, 10))

            x = int(x/10)

            if (reversedInteger > MAX/10 or (reversedInteger == MAX/10 and digit >= MAX % 10)):
                return 0

            if (reversedInteger < MIN/10 or (reversedInteger == MIN/10 and digit <= MIN % 10)):
                return 0

            reversedInteger = (reversedInteger*10) + digit

        return reversedInteger


if __name__ == "__main__":
    x = -123
    objectNums = Solution()
    print(objectNums.reverse(x))
