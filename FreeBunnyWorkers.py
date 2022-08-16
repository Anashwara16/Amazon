
# Free the bunny workers

import math
from itertools import combinations


class Solution:

    def freeBunny(self, numBuns: int, numRequired: int):

        distinctKeys = math.comb(numBuns, numRequired)

        numberOfCopies = (numBuns - numRequired + 1)


if __name__ == "__main__":
    bunny = Solution()
    print(bunny.freeBunny(5, 3))
