import random

def game():
    gamer= input("Enter your choices from 'r' for rock,'s' for scissors and 'p' for paper: \n")
    system= random.choice(['r','s','p'])

    if gamer==system:  #check if both the user and computer choice are same
        return 'TIE'

    if winner(gamer,system):  #call the function to check who won
        return 'User won :-)'
    
    return 'User Lost :-('



# rock > scissors, scissors > paper, paper > rock
def winner(gamer1, gamer2):  
    #the function will return true if gamer1 wins
    if (gamer1 =='r' and gamer2 =='s') or (gamer1=='s' and gamer2=='p') or (gamer1 =='p' and gamer2=='r'):
        # r>s,s>p, p>r
        return True



print(game())

