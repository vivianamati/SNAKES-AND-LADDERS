import random

class SnakesAndLadders:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [0] * num_players
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    def roll_die(self):
        return random.randint(1, 6)
    
    def move_player(self, player_index, steps):
        self.players[player_index] += steps
        if self.players[player_index] in self.snakes:
            print("Player", player_index + 1, "encountered a snake! They move from", self.players[player_index] - steps, "to", self.snakes[self.players[player_index]])
            self.players[player_index] = self.snakes[self.players[player_index]]
        elif self.players[player_index] in self.ladders:
            print("Player", player_index + 1, "found a ladder! They move from", self.players[player_index] - steps, "to", self.ladders[self.players[player_index]])
            self.players[player_index] = self.ladders[self.players[player_index]]
        elif self.players[player_index] > 100:
            self.players[player_index] -= steps
            print("Player", player_index + 1, "cannot move beyond 100!")
        else:
            print("Player", player_index + 1, "moves from", self.players[player_index] - steps, "to", self.players[player_index])
        
    def check_winner(self):
        for i, player in enumerate(self.players):
            if player == 100:
                return i
        return None

def main():
    num_players = int(input("Enter the number of players: "))
    game = SnakesAndLadders(num_players)
    winner = None
    while winner is None:
        for i in range(num_players):
            input("Player {} press Enter to roll the die: ".format(i + 1))
            steps = game.roll_die()
            print("Player", i + 1, "rolled a", steps)
            game.move_player(i, steps)
            winner = game.check_winner()
            if winner is not None:
                print("Player", winner + 1, "wins!")
                break

if __name__ == "__main__":
    main()
