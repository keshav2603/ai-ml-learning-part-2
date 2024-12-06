import random
# snake water gun game 
'''
rules:
1. snake win against water
2. water win against gun
3. gun win against snake
4. first to score 5 point will be winner 1win= 1 point
'''
"""
to calculate result 
0 = drow
-1 = computer win 
1 = player win

computer choice on x axis    
                                s   w   g
                            s   0   1   -1
player choice on y axis     w   -1  0   1
                            g    1  -1  0
"""
possibleResult = (
    (0,1,-1),
    (-1,0,1),
    (1,-1,0)
)
playerWin = 0
compWin = 0

def getRoundWinner(comp, player):
    winner = possibleResult[player][comp]
    global compWin 
    global playerWin 
    if(winner==-1):
        
        compWin= compWin + 1
        print(f"computer win!!!! your score:{playerWin},computer score:{compWin}")
    elif(winner==1):
       
        playerWin = playerWin + 1
        print(f"you win!!!! your score:{playerWin},computer score:{compWin}")
    else:
        print(f"it's a drow!!!! your score:{playerWin}, computer score:{compWin}")


def getMatchWinner():
    if(playerWin==5):
        print(f"you win the match by  {playerWin}:{compWin} score")
        return True
    elif(compWin==5):
        print(f"you loss the match by  {playerWin}:{compWin} score")
        return True
    else:
        return False
def getUserChoice():
    try:
        attack = int(input("type:\n0 for snake\n1 for water\n2 for gun\n"))
        return attack
    except:
        print("*****invalid choice*****")
        getUserChoice()

def getCompChoice():
    attack=[0,1,2]
    return random.choice(attack)

def showAttack(attack):
    if(attack==0):
        return "snake"
    elif(attack==1):
        return "water"
    elif( attack==2):
        return "gun"

while(not getMatchWinner()):
    userAttack = getUserChoice()
    compAttack = getCompChoice()
    print(f"your attack: {showAttack(userAttack)}")
    print(f"computer attack: {showAttack(compAttack)}")    
    getRoundWinner(compAttack,userAttack)
    print("**********NEXT*ROUND**********")