class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[" " for i in range(size)]for j in range(size)]


    def display(self):
        print(self.grid)

    def is_valid_move(self,row,col):
        if row < 0 or col < 0:
            return False
        try:
            if self.grid[row][col] != " ":
                    return False
            return True
        except IndexError:
            return False
        

    def place_move(self,row,col,symbol):
        if self.is_valid_move(row,col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self,symbol):
        for row in self.grid:
            if all(s == symbol for s in row):
                return True
        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size)):
                return True
        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True
        if all(self.grid[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True
        return False

    def check_draw(self):
        if not self.check_win("X") and not self.check_win("O"):
            if all(self.grid[i][j] != " " for i in range(self.size) for j in range(self.size)):
                return True
        return False

class Player:
    def __init__(self,symbol,name):
        self.symbol = symbol
        self.name = name
    
    def get_move(self,board):

        pass

class Game:
    def __init__(self,board,players,current_player_index):
        self.board = board
        self.players = players
        self.current_player_index = current_player_index
    
    def start(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            row, col = current_player.get_move(self.board)
            self.board.place_move(row, col, current_player.symbol)
            
            if self.board.check_win(current_player.symbol):
                self.board.display()
                break

            if self.board.check_draw():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
