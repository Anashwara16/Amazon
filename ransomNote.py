
# 383. Ransom Note

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomCount, magazineCount = {}, {}

        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)

        for r in ransomNote:
            if magazineCount[r] < ransomCount[r]:
                return False

        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "ab"
    objectNums = Solution()
    print(objectNums.canConstruct(ransomNote, magazine))
