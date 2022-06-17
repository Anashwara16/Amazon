
# 153. Find Minimum in Rotated Sorted Array


class Solution:
    def findMin(self, nums: list[int]) -> int:

        result = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:

            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right)//2

            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1

            else:
                right = mid - 1

        return result


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    objectNums = Solution()
    print(objectNums.findMin(nums))
