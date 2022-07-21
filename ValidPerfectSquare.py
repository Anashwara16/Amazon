
# 367. Valid Perfect Square


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 1, num

        while l <= r:

            mid = l + (r-l)//2

            if (mid*mid) == num:
                return True

            elif (mid*mid) > num:
                r = mid - 1

            else:
                l = mid + 1

        return False


if __name__ == "__main__":
    num = 17
    objectNums = Solution()
    print(objectNums.isPerfectSquare(num))
