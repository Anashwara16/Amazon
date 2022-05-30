
# 167. Two Sum II - Input Array Is Sorted


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        lo, hi = 0, len(numbers)-1

        while lo < hi:

            twosum = numbers[lo] + numbers[hi]

            if twosum == target:
                return [lo + 1, hi + 1]

            elif twosum < target:
                lo += 1

            elif twosum > target:
                hi -= 1

        return [-1, -1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    objectNums = Solution()
    print(objectNums.twoSum(numbers, target))
