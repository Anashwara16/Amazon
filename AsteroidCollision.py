
# 735. Asteroid Collision


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for a in asteroids:

            while stack and a < 0 and stack[-1] > 0:

                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()

                elif diff > 0:
                    a = 0

                else:
                    stack.pop()
                    a = 0

            if a:
                stack.append(a)

        return stack


if __name__ == "__main__":
    asteroids = [5, 10, -5]
    objectNums = Solution()
    print(objectNums.asteroidCollision(asteroids))
