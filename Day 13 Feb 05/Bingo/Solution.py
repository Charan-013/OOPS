    class BingoBoard:

        def __init__(self,board,marks):
            self.board = board
            self.marks = marks
            self.size = 5
        
        def markNumbers(self,calledNumbers):
            pass

        def isRowComplte(self,row):
            pass

        def isColumnComplete(self,col):
            pass

        def isMainDiagonalComplete(self):
            pass


        def isAntiDiagonalCompleted(self):
            pass

        def printBoard(self):
            pass

    class BingoGame:

        def __init__(self,board,calledNumbers):
            self.board = board
            self.calledNumbers = calledNumbers
            self.bingoLetters = "BINGO"
            self.letters = []

        def play(self):
            pass

        def strikeLetter(self):
            pass

        def printResult(self):
            pass

    
    board = []
    for i in range(5):
        line = list(map(int,input().split()))
        board.append(line)
            
    # print(board)

    values = list(map(int,input().rstrip().split(", ")))

    # print(values)
    boardInstance = BingoBoard(board)
    instance2 = BingoGame(boardInstance,values)

    BingoGame.play()
