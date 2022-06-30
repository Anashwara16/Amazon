
# 271. Encode and Decode Strings


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        resultString = ""

        for s in strs:
            resultString += str(len(s)) + "#" + s

        return resultString

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        resultList = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            stringLength = int(s[i:j])

            resultList.append(s[(j + 1): (j + 1 + stringLength)])

            i = j + 1 + stringLength

        return resultList


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


if __name__ == "__main__":
    dummy_input = ["Hello", "World"]
    objectNums = Solution()
    print(objectNums.encode(dummy_input))
