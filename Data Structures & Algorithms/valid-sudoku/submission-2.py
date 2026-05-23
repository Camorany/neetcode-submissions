class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            tempHashset = set()
            for element in row:
                if element != ".":
                    if element in tempHashset:
                        return False
                    tempHashset.add(element)

        for j in range(9):
            tempHashset = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in tempHashset:
                        return False
                    tempHashset.add(board[i][j])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                tempHashset = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            if board[i + k][j + l] in tempHashset:
                                return False
                            tempHashset.add(board[i + k][j + l])  
        
        return True

