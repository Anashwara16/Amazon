
# 525. Contiguous Array


from tkinter import N


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:

        maxLength = 0
        total = 0
        hashMap = {}

        for i in range(len(nums)):

            current = nums[i]

            if current == 0:
                total -= 1
            else:
                total += 1

            if total == 0:
                maxLength = i + 1

            if total in hashMap:
                maxLength = max(maxLength, i - hashMap[total])
            else:
                hashMap[total] = i

        return maxLength


if __name__ == "__main__":
    nums = [0, 1]
    objectNums = Solution()
    print(objectNums.findMaxLength(nums))
