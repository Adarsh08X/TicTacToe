import itertools


def win(game):
    def equal(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False
    #Horizontal
    for row in game:
        if equal(row):
            print(f"Player {row[0]} is the winner!^_^")
            return True
    #Diagonal
    diag=[]
    for row,col in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
    if equal(diag):
        print(f"Player {diag[0]} is the Winner!^_^")
        return True
    
    diag = []
    for i in range(len(game)):
        diag.append(game[i][i])
    if equal(diag):
        print(f"Player {diag[0]} is the Winner!^_^")
        return True
    
    #Vertical
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
        if equal(check):
            print(f"Player {check[0]} is the Winner!^_^")
            return True
    
    return False    


def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try: 
        if game_map[row][column]!= 0:
            print("This position is already occupied! Choose another")
            return game_map,False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column]=player
        for count,row in enumerate(game):
            print(count,row)
        return game_map,True
    except IndexError as e:
        print("Error:Make sure you input row/column as 0,1 or 2.",e)
        return game_map,False
    except Exception as e:
        print("Something went wrong",e)
        return game_map,False
    
    
play=True
#players=[1,2]
while play:
    game=[[0,0,0],[0,0,0],[0,0,0]]
    player_choice=itertools.cycle([1,2])
    game,_=game_board(game,just_display=True)
    game_won=False
    while not game_won:
        current_player=next(player_choice)
        print("Current Player is: ",current_player)
        played=False
        while not played:  
           col_choice=int(input("What column you want to chose?(0,1 or 2): "))
           row_choice=int(input("What row you want to chose?(0,1 or 2): "))
           game,played=game_board(game,current_player,row_choice,col_choice)
           
        if win(game):
            game_won=True
            again=input("The game is over would you like to play again?(y/n) ")
            if again.lower()=="y":
                print("Restarting....")
            elif again.lower()=="n":
                print("See you later!")
                play=False
            else:
                print("Not a valid answer , see u later!")
                play=False
        