class BingoBoard:
    SIZE = 5

    def __init__(self, board, marks=None):
        self.board = board
        self.marks = [["" for _ in range(BingoBoard.SIZE)] for _ in range(BingoBoard.SIZE)] if marks is None or marks == [] else marks

    def markNumbers(self, calledNumbers):
        for i in range(BingoBoard.SIZE):
            for j in range(BingoBoard.SIZE):
                if self.board[i][j] in calledNumbers:
                    self.marks[i][j] = "X"

    def isRowComplete(self, row):
        return all(self.marks[row][j] == "X" for j in range(BingoBoard.SIZE))

    def isColumnComplete(self, col):
        return all(self.marks[i][col] == "X" for i in range(BingoBoard.SIZE))

    def isMainDiagonalComplete(self):
        return all(self.marks[i][i] == "X" for i in range(BingoBoard.SIZE))

    def isAntiDiagonalComplete(self):
        return all(self.marks[i][BingoBoard.SIZE - 1 - i] == "X" for i in range(BingoBoard.SIZE))

    def printBoard(self):
        for i in range(BingoBoard.SIZE):
            print("  ".join("X" if self.marks[i][j] == "X" else str(self.board[i][j]) for j in range(BingoBoard.SIZE)))

class BingoGame:
    LETTERS = ["B", "I", "N", "G", "O"]

    def __init__(self, board, calledNumbers, bingoLetters=None):
        self.board = board
        self.calledNumbers = calledNumbers
        self.bingoLetters = [] if bingoLetters is None else bingoLetters

    def strikeLetter(self):
        if len(self.bingoLetters) < len(BingoGame.LETTERS):
            self.bingoLetters.append(BingoGame.LETTERS[len(self.bingoLetters)])

    def play(self):
        self.board.markNumbers(self.calledNumbers)
        for i in range(BingoBoard.SIZE):
            if self.board.isRowComplete(i):
                self.strikeLetter()
        for j in range(BingoBoard.SIZE):
            if self.board.isColumnComplete(j):
                self.strikeLetter()
        if self.board.isMainDiagonalComplete():
            self.strikeLetter()
        if self.board.isAntiDiagonalComplete():
            self.strikeLetter()

    def printResult(self):
        self.board.printBoard()
        print()
        if len(self.bingoLetters) == 5:
            letters_str = ""
            for letter in self.bingoLetters:
                letters_str += letter + " "
            print(letters_str.strip())
            print("Game Completed!")
        else:
            remaining = ""
            for letter in BingoGame.LETTERS[len(self.bingoLetters):]:
                remaining += letter + " "
            print("Remaining Letters: " + remaining.strip())

def main():
    board_nums = [list(map(int, input().split())) for _ in range(5)]
    board = BingoBoard(board_nums, [])
    calledNumbers = list(map(int, input().replace(" ", "").split(",")))
    game = BingoGame(board, calledNumbers, [])
    game.play()
    game.printResult()

if __name__ == "__main__":
    main()


