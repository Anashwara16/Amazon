
#79. Word Search

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r,c,i):
        
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                word[i] != board[r][c] or
                (r, c) in path
                ):
                return False
        
            path.add((r,c))
                
            res = ( dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1) 
                   )
                
            path.remove((r,c))
            
            return res
        
        for r in range(rows): 
            for c in range(cols): 
                print("***INSIDE 2 FOR LOOPS: ***")
                if dfs(r,c,0):
                    return True
                
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    objectNums = Solution()
    print(objectNums.exist(board, word))