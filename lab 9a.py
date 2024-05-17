#GUILLERMINA MARTO

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

beats = {'rock': 'sissors',
         'sissors': 'paper',
         'paper': 'rock'}

from numpy import random

# First try: globals

choices = ['rock', 'paper', 'scissors']
beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

p1 = random.choice(choices)
p2 = random.choice(choices)

print(f'Player 1: {p1}\nPlayer 2: {p2}')

if beats[p1] == p2:
    print('Player 1 wins!')
elif beats[p2] == p1:
    print('Player 2 wins!')
else:
    print('Tie.')


# Second try: functions

def find_winner(p1, p2):
    if beats[p1] == p2:
        return 'Player 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins!'
    else:
        return 'Tie.'

def readysetgo():
    return random.choice(choices)

def play_once():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'Player 1: {p1}\nPlayer 2: {p2}')
    
    winner = find_winner(p1, p2)
    print(f'The winner is: {winner}')

# Using classes

class Player:
    def __init__(self, name, strategy='random'):
        self.name = name
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.strategy = strategy

    def readysetgo(self):
        if self.strategy == 'random':
            return random.choice(self.choices)
        elif self.strategy == 'always_rock':
            return 'rock'
        else:
            return input(f'{self.name}, pick one of rock, paper, or scissors: ').strip().lower()

class Game:
    def __init__(self, num_players=2):
        self.beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        self.num_players = num_players
        self.players = [Player(f'Player {i + 1}', strategy=('human' if i < num_players else 'random')) for i in range(2)]

    def find_winner(self, p1_choice, p2_choice):
        if self.beats[p1_choice] == p2_choice:
            return 1  # Player 1 wins
        elif self.beats[p2_choice] == p1_choice:
            return 2  # Player 2 wins
        else:
            return 0  # Tie

    def play_once(self):
        p1_choice = self.players[0].readysetgo()
        p2_choice = self.players[1].readysetgo()
        print(f'Player 1: {p1_choice}\nPlayer 2: {p2_choice}')
        
        winner = self.find_winner(p1_choice, p2_choice)
        if winner == 1:
            print('The winner is: Player 1!')
            self.players[0].wins += 1
        elif winner == 2:
            print('The winner is: Player 2!')
            self.players[1].wins += 1
        else:
            print('The result is a Tie!')

    def play_series(self, rounds):
        for _ in range(rounds):
            self.play_once()
        print(f'\nFinal Results:\nPlayer 1 wins: {self.players[0].wins}\nPlayer 2 wins: {self.players[1].wins}')

# Example usage
if __name__ == "__main__":
    num_human_players = int(input('Enter number of human players (0, 1, or 2): '))
    game = Game(num_players=num_human_players)

    while True:
        game.play_once()
        play_again = input('Do you want to play again? (yes/no): ').strip().lower()
        if play_again != 'yes':
            break

    print(f'\nFinal Results:\nPlayer 1 wins: {game.players[0].wins}\nPlayer 2 wins: {game.players[1].wins}')






















def find_winner (p1, p2):
    if beats[p1] = p2:
        return 'Player 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins!'
    else:
        return 'Tie.'
    
def readysetgo():
    return random.choice(choices)

def play_once():
    p1 = readysetgo()
    p2 = readysetgo()


class player:
    def __init__(self, name, strategy ='random'):
        self.name = name
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.strategy = strategy
        


class game:
    def __init__(self, game):
        self.game = game

        
