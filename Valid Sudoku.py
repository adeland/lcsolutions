class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def dupe(arr):
            seen = set()
            for ele in arr:
                if ele != "." and ele in seen:
                    return True
                seen.add(ele)
            return False    
        for i in range(9):
            if dupe(board[i]):
                return False    
        for j in range(9):
            c = [board[i][j] for i in range(9)]
            if dupe(c):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if dupe(s):
                    return False
        return True
