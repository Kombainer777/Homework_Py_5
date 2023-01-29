field = [1,2,3,
        4,5,6,
        7,8,9]

win_lines = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_maps():
    print(field[0], end = " ")
    print(field[1], end = " ")
    print(field[2])
 
    print(field[3], end = " ")
    print(field[4], end = " ")
    print(field[5])
 
    print(field[6], end = " ")
    print(field[7], end = " ")
    print(field[8])
 

def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol

def get_result():
    win = ""
 
    for i in win_lines:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"   
             
    return win

game_over = False
player1 = True
 
while game_over == False:

    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
 
    step_field(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
        
print_maps()
print("Победил", win)