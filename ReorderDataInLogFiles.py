
# 937. Reorder Data in Log Files


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        def sortingAlgorithm(log):

            lhs, rhs = log.split(" ", 1)

            if rhs[0].isalpha():
                return (0, rhs, lhs)

            else:
                return (1, )

        return sorted(logs, key=sortingAlgorithm)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    objectNums = Solution()
    print(objectNums.reorderLogFiles(logs))
