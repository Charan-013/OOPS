class LuckyBingoBoard:

    def __init__(self,size,board):
        self.size = size
        self.board = board
        self.marks = [[False] * self.size for i in range(self.size)]
    
    def mark_number(self,num):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == num:
                    self.marks[i][j] = True
                # else:
                #     self.marks[i][j] = self.board[i][j]
                    break

    def is_row_complete(self,row):
        count = 0
        for j in range(self.size):
            if self.marks[row][j] == True:
                count += 1
        return count == self.size
        # if count == self.size:
        #     return True
        # else:
        #     return False

    def is_column_completed(self,column):
        for i in range(self.size):
            if self.marks[i][column] != True:
                return False
        return True

    def is_main_diagonal_complete(self):
        if all(self.marks[i][i] == True for i in range(self.size)):
            return True
        return False
    
    def is_anti_diagonal_complete(self):
        if all(self.marks[n][self.size - 1 - n] == True for n in range(self.size)):
            return True
        return False

    def is_cross_complete(self):
        pass

    def check_win(self):
        # print(self.marks)
        for i in range(self.size):
            if self.is_row_complete(i):
                return True
        for j in range(self.size):
            if self.is_column_completed(j):
                return True
        if self.is_main_diagonal_complete():
            return True
        if self.is_anti_diagonal_complete():
            return True
        # if self.is_cross_complete():
        #     return True
        return False

    def print_board(self):
        print("Board State:")
        for i in range(self.size):
            print(" ".join("X" if self.marks[i][j] else str(self.board[i][j]) for j in range(self.size)))


class Player:

    def __init__(self,name,board):
        self.name = name
        self.board = board

    def mark_number(self,num):
        self.board.mark_number(num)

    def has_won(self):
        # print(self.board.check_win())
        # if self.board.check_win():
        #     return True
        # return False
        return self.board.check_win()
    
    
    def display_board(self):
        print(f"{self.name}'s Board:")
        self.board.print_board()


class LuckyBingoGame:
    def __init__(self,players,predefined_numbers):
        self.players = players
        self.predefined_numbers = predefined_numbers
        self.current_index = 0

    def play(self):
        ci = 0
        hs = False
        while not hs:
            currentplayer = self.players[ci]
            # print(self.predefined_numbers)
            print(f"{currentplayer.name} calls number: {self.predefined_numbers[self.current_index]}")
            for p in self.players:
                p.mark_number(self.predefined_numbers[self.current_index])
            # play_turn = player.mark_number(self.predefined_numbers[self.current_index])
            for p in self.players:
                p.display_board()
            for p in self.players:
                if p.has_won():
                    if p == currentplayer:
                        print(f"{p.name} Wins!")
                        hs = True
                        break
            if self.current_index  == len(self.predefined_numbers) - 1:
                break
            self.current_index = self.current_index + 1
            ci = (ci + 1) % len(self.players)
