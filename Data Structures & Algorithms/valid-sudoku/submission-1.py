class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            tempHashset = set()
            for element in row:
                if element != ".":
                    if element in tempHashset:
                        print(element)
                        print(f"{element} is false, returning")
                        return False
                    tempHashset.add(element)

        for j in range(9):
            tempHashset = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in tempHashset:
                        print(board[i][j])
                        print(f"{board[i][j]} (board row:{i} col:{j} ) is false, returning")
                        return False
                    tempHashset.add(board[i][j])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                tempHashset = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            print(board[i + k][j + l])
                            print(f"{board[i + k][j + l]} (board row:{i + k} col:{j + l} ) is false, returning")
                            if board[i + k][j + l] in tempHashset:
                                return False
                            tempHashset.add(board[i + k][j + l])  
        
        return True

