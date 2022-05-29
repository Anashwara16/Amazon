
# 12. Integer to Roman


class Solution:
    def intToRoman(self, num: int) -> str:

        romanList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50],
                     ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        result = ""

        for roman, number in reversed(romanList):

            if num // number:
                count, num = divmod(num, number)
                result += (roman * count)

        return result


if __name__ == "__main__":
    num = 1994
    objectNums = Solution()
    print(objectNums.intToRoman(num))
