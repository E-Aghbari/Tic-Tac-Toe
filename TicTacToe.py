class Game:
    game_over = False

    players = []

    grids = {"Top left": " ", "Top": " ", "Top right": " ", "Mid left": " ", "Mid": " ", "Mid right": " ", "Bottom left": " " , "Bottom": " ", "Bottom right": " "}

    rounds = 0

    def print_board(self):
        

        print( "           |           |         ")
        print("     {}     |     {}     |     {}    ".format(Game.grids["Top left"], Game.grids["Top"], Game.grids["Top right"]))
        print( "           |           |         ")
        print("---------------------------------")
        print( "           |           |         ")
        print("     {}     |     {}     |     {}    ".format(Game.grids["Mid left"], Game.grids["Mid"], Game.grids["Mid right"]))
        print( "           |           |         ")
        print("----------------------------------")
        print( "           |           |         ")
        print("     {}     |     {}     |     {}    ".format(Game.grids["Bottom left"], Game.grids["Bottom"], Game.grids["Bottom right"]))
        print( "           |           |         ")
        
        game.check_win(player1, player2)
    
    def add_players(self):
        if type(self) is Player:
            Game.players.append(self)

    def check_win(self, player1, player2):
        if Game.grids["Top left"] == Game.grids["Top"] == Game.grids["Top right"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Mid left"] == Game.grids["Mid"] == Game.grids["Mid right"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Bottom left"] == Game.grids["Bottom"] == Game.grids["Bottom right"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] == Game.grids["Mid left"] == Game.grids["Bottom left"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top"] == Game.grids["Mid"] == Game.grids["Bottom"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top right"] == Game.grids["Mid right"] == Game.grids["Bottom right"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] == Game.grids["Mid"] == Game.grids["Bottom right"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top right"] == Game.grids["Mid"] == Game.grids["Bottom left"] == player1.symbol:
            print(f"{player1.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] == Game.grids["Top"] == Game.grids["Top right"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Mid left"] == Game.grids["Mid"] == Game.grids["Mid right"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Bottom left"] == Game.grids["Bottom"] == Game.grids["Bottom right"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] == Game.grids["Mid left"] == Game.grids["Bottom left"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top"] == Game.grids["Mid"] == Game.grids["Bottom"] == player2.symbol: 
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top right"] == Game.grids["Mid right"] == Game.grids["Bottom right"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] == Game.grids["Mid"] == Game.grids["Bottom right"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top right"] == Game.grids["Mid"] == Game.grids["Bottom left"] == player2.symbol:
            print(f"{player2.name} has won")
            Game.game_over = True
        elif Game.grids["Top left"] != " " and Game.grids["Top"] != " " and Game.grids["Top right"] != " " and Game.grids["Mid left"] != " " and Game.grids["Mid"] != " " and Game.grids["Mid right"] != " " and Game.grids["Bottom left"] != " " and Game.grids["Bottom"] != " " and Game.grids["Bottom right"] != " ":
            print("It's a tie")
            Game.game_over = True



    def new_rounds(self):
        Game.rounds += 1
        print(f"{Game.rounds} has started.")

    def __repr__(self) -> str:
        return f"This game called Tic Tac Toe its comprised of {len(Game.grids)} grids and {len(Game.players)} players. First player fills three grids in one row, wins."
 

class Player:
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol
        Game.add_players(self)
    
    def choose_grid(self, grid):
        if Game.grids[grid] != " ":
            grid = input( "Nah bro. Choose another one\n")
            self.choose_grid(grid)

        if Game.grids[grid] == " ":
            self.print_move(grid)

    def print_move(self, grid):
        Game.grids[grid] = self.symbol
        

    def __repr__(self) -> str:
        return f"{self.name}"

player1 = Player("Ebrahim", "X")
player2 = Player("Abdullah", "O")

game = Game()
game.print_board()

while not game.game_over:
    chosen_grid = input(f"Choose a grid {player1.name}\n")
    player1.choose_grid(chosen_grid)
    game.print_board()
    if game.game_over:
        break
    chosen_grid = input(f"Choose a grid {player2.name}\n")
    player2.choose_grid(chosen_grid) 
    game.print_board()

    
    