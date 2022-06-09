
# 165. Compare Version Numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        nums1 = version1.split('.')
        nums2 = version2.split('.')
        print(nums1)
        print(nums2)
        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(max(n1, n2)):

            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            print("i1: ", i1)
            print("i2: ", i2)
            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


if __name__ == "__main__":
    version1 = "1.01"
    version2 = "1.001"
    objectNums = Solution()
    print(objectNums.compareVersion(version1, version2))
