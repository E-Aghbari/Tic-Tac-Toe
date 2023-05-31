class Game:
    game_over = False

    players = []

    start = [0 for i in range(9)]

    grids = {"Top left": start[0], "Top": start[1], "Top right": start[2], "Mid left": start[3], "Mid": start[4], "Mid right": start[5], "Bottom left": start[6] , "Bottom": start[7], "Bottom right": start[8]}

    row = 3
    column = 3

    rounds = 0

    def print_board(self, symbol = None):

        for i in range(12):
            print("        |               |    ")
            if i == 3 or i== 7:
                print(" ------------------------------")
    
    def add_players(self):
        if type(self) is Player:
            Game.players.append(self)

    def check_win():
        print(Game.start)
        if sum(Game.start[:3]) or sum(Game.start[3:6]) or sum(Game.start[6:]) or (Game.start[0] + Game.start[4] + Game.start[8]) or (Game.start[2] + Game.start[4] + Game.start[6]) == 3:
            Game.game_over = True
            print(f"Game Over")

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
        print(Game.start)
        print(Game.grids)
        if Game.grids[grid] == 1:
            return "This grid is already taken."
        if grid in Game.grids.keys():
            Game.start[0] = 1
            self.print_move(grid)


            

    def print_move(self, grid):
        pass

    def take_turn(self):
        pass

    def __repr__(self) -> str:
        return f"{self.name}"

player1 = Player("Ebrahim", "X")
player2 = Player("Abdullah", "O")

game = Game()
game.print_board()

while not Game.game_over:
    chosen_grid = input(f"Choose a grid {player1.name}")
    player1.choose_grid(chosen_grid)
    chosen_grid = input(f"Choose a grid {player2.name}")
    player2.choose_grid(chosen_grid) 

    
    Game.check_win()