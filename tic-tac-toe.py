def printboard(board):
    print('       |        |        ')
    print('   '+board[7]+'   |   '+board[8]+'    |    '+board[9]+'   ') 
    print('       |        |        ')
    print('-------------------------')
    print('       |        |        ')
    print('   '+board[4]+'   |   '+board[5]+'    |    '+board[6]+'   ')
    print('       |        |        ')
    print('-------------------------')   
    print('       |        |        ')
    print('   '+board[1]+'   |   '+board[2]+'    |    '+board[3]+'   ')
    print('       |        |        ')
    
    


def check_win(board):
    if(board[1] == board[2] == board[3] != ' ' ):
        return 1
    elif(board[4] == board[5] == board[6] != ' ' ):
        return 1
    elif(board[7] == board[8] == board[9] != ' ' ):
        return 1
    elif(board[1] == board[4] == board[7] != ' ' ):
        return 1
    elif(board[2] == board[5] == board[8] != ' ' ):
        return 1
    elif(board[3] == board[6] == board[9] != ' ' ):
        return 1
    elif(board[1] == board[5] == board[9] != ' ' ):
        return 1
    elif(board[3] == board[5] == board[7] != ' ' ):
        return 1
    else:
        return 0;
    
      
    
def check_place(board,n):
    if(board[n]=='X' or board[n]=='O'):
        return 0
    else:
        return 1

    
def place_player1(board):
    print('player1 enter your move(1-9):')
    position = int(input())
    
    if(position<10 and position>0):      
        while(check_place(board,position) == 0):
            print('position occupied , enter your move again(1-9):')
            position = int(input())
    else:
        print('wrong position! Please enter a number between 1-9')
        place_player1()
        
    return position
    
def place_player2(board):
    print('player2 enter your move(1-9):')
    position = int(input())
    
    if(position<10 and position>0):      
        while(check_place(board,position) == 0):
            print('position occupied , enter your move again(1-9):')
            position = int(input())
    else:
        print('wrong position! Please enter a number between 1-9')
        place_player1()
        
    return position
    
    
def board_full(board):
    for i in board:
        if(i == ' '):
            return 0
    return 1
        
    
    
theboard=[' ']*10
theboard[0]='#'

print('The rules are : Your numpad is your position key. Like this:')
print('  7|8|9         | | ')
print('  -----        -----')
print('  4|5|6         | | ')
print('  -----        -----')
print('  1|2|3         | | ')

while(1):
    print('Who is player1 (X / O) :' )
    player1 = input()
    player1 = player1.upper()

    if(player1 == 'X'):
        player2='O'
    else:
        player2='X'

    while(1):
        print('Are you ready ?(Y/N):')
        ready= input().lower()
        if(ready.startswith('y')):
            break;
            
    while(1):
        theboard[place_player1(theboard)] = player1
        printboard(theboard)
        
        if(check_win(theboard) != 0):
            print('player1 wins!')
            break
        elif(board_full(theboard)==1):
            print('its a tie!')
            break
        
        theboard[place_player2(theboard)] = player2 
        printboard(theboard)
        
        if(check_win(theboard) != 0):
            print('player2 wins!')
            break
        elif(board_full(theboard)==1):
            print('its a tie!')
            break
    
    print('do you want to play again?(Y/N):')
    play_again = input().lower()
    
    if(play_again.startswith('y')):
        theboard =[' ']*10
        theboard[0] = '#'
    else:
        break
    
print('thank you for playing')


    



    
    


    
    

        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
