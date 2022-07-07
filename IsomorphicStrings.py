
# 205. Isomorphic Strings


class Solution:

    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        print(new_str)
        print(" ".join(new_str))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


if __name__ == "__main__":
    s = "egg"
    t = "add"
    objectNums = Solution()
    print(objectNums.isIsomorphic(s, t))
