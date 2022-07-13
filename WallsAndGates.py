
# 286. Walls and Gates


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def addRooms(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or rooms[r][c] == -1 or rooms[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])

        distance = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:

            for i in range(len(q)):

                qr, qc = q.popleft()

                rooms[qr][qc] = distance

                for dr, dc in directions:
                    row, col = qr + dr, qc + dc
                    addRooms(row, col)

            distance += 1


if __name__ == "__main__":
    rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
    objectNums = Solution()
    print(objectNums.wallsAndGates(rooms))
