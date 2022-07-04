# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = {}, {}

        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

        l = 0

        for r in range(len(s1), len(s2)):

            if s1Count == s2Count:
                return True

            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            s2Count[s2[l]] -= 1

            if s2Count[s2[l]] == 0:
                s2Count.pop(s2[l])
            l += 1

        return True if (s1Count == s2Count) else False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    objectNums = Solution()
    print(objectNums.checkInclusion(s1, s2))
