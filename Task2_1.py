import time
txt = 'Добро пожаловать в игру "2021 конфета!"'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)
print()
print()
time.sleep(2)

def Competition(*params):
    global player1, player2, sweets, count_round
    a: int = input(txt1)
    while int(a) > 28:
        a: int = input(txt_correct)
    else:
        if (int(sweets) - int(a)) <= 0:
            sweets = int(sweets) - int(a)
            player1 = int(player1) + int(player2)
            print('Игрок №1 победил в раунде №', count_round, ' и забрал ВСЕ конфеты!')
        else:
            (int(sweets) - int(a)) > 0
            sweets = int(sweets) - int(a)
            player1 = int(player1) + int(a)
            print ('Игрок 1 взял', a, ' конфет. У игрока сейчас', player1, ' штук. На столе осталось', sweets, ' конфет')
            print()
        

    if sweets > 0:
        b: int = input(txt2)
        while int(b) > 28:
            b: int = input(txt_correct)
        else:
            if (int(sweets) - int(b)) <= 0:
                sweets = int(sweets) - int(b)
                player2 = int(player1) + int(player2)
                print('Игрок №2 победил в раунде №', count_round, ' и забрал ВСЕ конфеты!')
            else:
                sweets = int(sweets) - int(b)
                player2 = int(player2) + int(b)
                print ('Игрок 2 взял', b, ' конфет. У игрока сейчас', player2, ' штук. На столе осталось', sweets, ' конфет')
                print()
        
                
    param = [int(player1), int(player2), int(sweets), int(count_round)]
    count_round +=1
    return param


player1: int = 0
player2: int = 0
sweets: int = 100
count_round: int = 1
txt1 = 'Ходит первый игрок. Сколько хотите взять себе конфет со стола? (максимум можно взять 28 штук за 1 ход):  '
txt_correct = 'Введите корректное значение (не более 28 штук за 1 ход):  '
txt2 = 'Очередь второго игрока. Сколько хотите взять себе конфет со стола? (максимум можно взять 28 штук за 1 ход):  '
param = [player1, player2, sweets, count_round]

if sweets > 0:
    print('Раунд №', count_round)
    while sweets > 0:
        Competition(player1, player2, sweets, count_round)

    



    
    
    