#Juego 3 Rock, Paper, Sicssors
import random

def play():
    user= input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n ") # \n is to make a line break
    option_list=['r','p','s']
    computer= random.choice(option_list)
    
    if user==computer:
        return 'It\'s a tie' #return breaks the function as it is for break for while
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'   
    #r>s, s>p, p>r
def is_win(player, opponent):
    # return True if player wins
    if (player == 'r' and opponent == 's') or (player =='s' and opponent=='p') \
        or (player =='p' and opponent=='r'):
            return True

print(play())