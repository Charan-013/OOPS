class BingoBoard:
    SIZE = 5

    def __init__(self, board, marks):
        self.board = board
        if marks is None or marks == []:
            self.marks = []
            for n in range(BingoBoard.SIZE):
                row = []
                for j in range(BingoBoard.SIZE):
                    row.append("")
                self.marks.append(row)
        else:
            self.marks = marks

    def markNumbers(self, calledNumbers):
        for n in range(BingoBoard.SIZE):
            for m in range(BingoBoard.SIZE):
                if self.board[n][m] in calledNumbers:
                    self.marks[n][m] = "X"

    def isRowComplete(self, row):
        count = 0
        for j in range(BingoBoard.SIZE):
            if self.marks[row][j] == "X":
                count += 1
        if count == BingoBoard.SIZE:
            return True
        else:
            return False

    def isColumnComplete(self, column):
        for i in range(BingoBoard.SIZE):
            if self.marks[i][column] != "X":
                return False
        return True

    def isMainDiagonalComplete(self):
        for n in range(BingoBoard.SIZE):
            if self.marks[n][n] != "X":
                return False
        return True

    def isAntiDiagonalComplete(self):
        for n in range(BingoBoard.SIZE):
            if self.marks[n][BingoBoard.SIZE - 1 - n] != "X":
                return False
        return True

    def printBoard(self):
        for n in range(BingoBoard.SIZE):
            line = ""
            for m in range(BingoBoard.SIZE):
                if self.marks[n][m] == "X":
                    line += "X"
                else:
                    line += str(self.board[n][m])
                if m < BingoBoard.SIZE - 1:
                    line += "  "
            print(line)


class BingoGame:
    LETTERS = ["B", "I", "N", "G", "O"]

    def __init__(self, board, calledNumbers, bingoLetters):
        self.board = board
        self.calledNumbers = calledNumbers
        self.bingoLetters = bingoLetters

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
        letters_str = ""
        for letter in self.bingoLetters:
            letters_str += letter + " "
        letters_str = letters_str.strip()
        if len(self.bingoLetters) == 5:
            print(letters_str)
            print("Game Completed!")
        else:
            remaining = ""
            for letter in BingoGame.LETTERS[len(self.bingoLetters) :]:
                remaining += letter + " "
            remaining = remaining.strip()
            print("Remaining Letters: " + remaining)


def main():

    new = []

    for i in range(5):
        new.append(list(map(int, input().split())))

    board = BingoBoard(new, [])

    calledNumbers = list(map(int, input().split(", ")))

    bingo1 = BingoGame(board, calledNumbers, [])
    bingo1.play()
    bingo1.printResult()


if __name__ == "__main__":
    main()
