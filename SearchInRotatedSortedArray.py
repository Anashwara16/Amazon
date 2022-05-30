
# 33. Search in Rotated Sorted Array


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:

                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                else:
                    r = mid - 1

            else:

                if target < nums[mid] or target > nums[r]:
                    r = mid - 1

                else:
                    l = mid + 1

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    objectNums = Solution()
    print(objectNums.search(nums, target))
