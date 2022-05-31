# 212. Word Search II


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def addWord(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.isEndOfWord = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])

        result, visited = set(), set()

        def dfs(r, c, node, word):

            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] not in node.children or (r, c) in visited:
                return

            node = node.children[board[r][c]]

            word += board[r][c]

            flag = True

            if node.isEndOfWord:
                result.add(word)
                if len(node.children) == 0:
                    del node
                    flag = False

            if flag:
                visited.add((r, c))
                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)
                visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
             ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    objectNums = Solution()
    print(objectNums.findWords(board, words))
