# 50. Pow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def expo(x, n):

            if x == 0:
                return 0
            if x == 1:
                return 1
            if n == 0:
                return 1

            result = expo(x, n//2)
            print("Result BEFORE =>", result)
            result = result * result
            print("Result AFTER =>", result)
            print("N AFTER =>", n)
            return (x * result) if (n % 2) else result

        result = expo(x, abs(n))

        return result if (n >= 0) else (1/result)


if __name__ == "__main__":
    x = 2.00000
    n = 10
    objectNums = Solution()
    print(objectNums.myPow(x, n))
