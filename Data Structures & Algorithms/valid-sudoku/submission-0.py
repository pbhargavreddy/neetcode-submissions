class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isRow(row):
            freq = [False]*10
            for i in range(9):
                if board[row][i] == '.':
                    continue
                idx = int(board[row][i])
                if freq[idx]:
                    return False
                freq[idx] = True
            return True
        def isCol(col):
            freq = [False]*10
            for i in range(9):
                if board[i][col] == '.':
                    continue
                idx = int(board[i][col])
                if freq[idx]:
                    return False
                freq[idx] = True
            return True
        def isBox(i,j):
            freq = [False]*10
            for row in range(i,i+3):
                for col in range(j,j+3):
                    if board[row][col] == '.':
                        continue
                    idx = int(board[row][col])
                    if freq[idx]:
                        return False
                    freq[idx] = True
            return True
        # check
        for i in range(9):
            if isRow(i) and isCol(i):
                continue
            else:
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                if isBox(i,j) == False:
                    return False
        return True
                