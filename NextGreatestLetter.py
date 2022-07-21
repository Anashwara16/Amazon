
# 744. Find Smallest Letter Greater Than Target


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        n = len(letters)
        l, r = 0, n
        newTarget = ord(target)

        while l < r:

            mid = l + (r-l)//2
            print(l, r, mid)
            midValue = ord(letters[mid])

            if midValue <= newTarget:
                l = mid + 1

            else:
                r = mid

        print(l, n)
        print(l % n)
        return letters[l % n]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "c"
    objectNums = Solution()
    print(objectNums.nextGreatestLetter(letters, target))
