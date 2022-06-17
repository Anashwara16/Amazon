
# 69. Sqrt(x)


class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left, right = 2, x//2

        while left <= right:

            mid = left + (right-left) // 2
            num = mid * mid

            if num < x:
                left = mid + 1

            elif num > x:
                right = mid - 1

            else:
                return mid

        return right


if __name__ == "__main__":
    x = 4
    objectNums = Solution()
    print(objectNums.mySqrt(x))
