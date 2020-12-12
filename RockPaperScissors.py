import random

def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n" )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "it\'s a tie"

    if winner(user, computer):
        return 'You won!'

    return 'you lost'

def winner(player, opponent):
    #return trye if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())