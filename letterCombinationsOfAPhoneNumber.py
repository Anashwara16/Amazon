
# 17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if len(digits) == 0:
            return []

        result = []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, currentString):

            if len(currentString) == len(digits):
                result.append(currentString)
                print("Same size as digits: ", currentString, result)
                return

            for c in letters[digits[i]]:
                print("*** New iteration ***")
                print("Iteration: ", i)
                print("Current string: ", currentString)
                print("Character: ", c)
                backtrack(i+1, currentString + c)
                print("Current string after BT - ", currentString)

        print("1st backtrack")
        backtrack(0, "")

        return result


if __name__ == "__main__":
    digits = "23"
    objectNums = Solution()
    print(objectNums.letterCombinations(digits))
