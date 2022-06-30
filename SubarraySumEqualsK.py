
# 560. Subarray Sum Equals K


from ast import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        currentSum = 0
        prefixSums = {0: 1}

        for n in nums:

            currentSum += n

            diff = currentSum - k

            result += prefixSums.get(diff, 0)

            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)

        return result


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    objectNums = Solution()
    print(objectNums.subarraySum(nums, k))
