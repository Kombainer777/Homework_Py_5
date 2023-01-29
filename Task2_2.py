import random
import time

def Player1(*params):           # Алгоритм ходов игрока
    global player1, ai, sweets, count_round
    a: int = input(txt1)
    while int(a) > 28:
        a: int = input(txt_correct)
    else:
        if (int(sweets) - int(a)) <= 0:
            sweets = int(sweets) - int(a)
            player1 = int(player1) + int(ai)
            print('Игрок 1 забрал', a, ' конфет, на столе осталось', sweets,'! штук Игрок 1 победил в раунде № ', count_round, ' и забрал ВСЕ конфеты!')
        else:
            (int(sweets) - int(a)) > 0
            sweets = int(sweets) - int(a)
            player1 = int(player1) + int(a)
            print ('Игрок 1 взял', a, ' конфет. У игрока сейчас', player1, ' штук. На столе осталось', sweets, ' конфет')
            print()
    param = [int(player1), int(ai), int(sweets)]
    return param


def ai_step(*params):           # Разбил ходы ИИ для того чтобы можно было эти шаги засунуть в генератор вероятностей. Обычный шаг, когда много конфет на столе
    global  player1, ai, sweets, count_round
    b: int = random.randint(1,29)
    sweets = int(sweets) - int(b)
    ai = int(ai) + int(b)
    print ('ИИ взял', b, ' конфет. У игрока сейчас', ai, ' штук. На столе осталось', sweets, ' конфет')
    print()

def danger_step(*params):      # 2-е разбитие на функции ходов ИИ. Шаг, чтобы поставить "Шах" игроку
    global player1, ai, sweets, count_round
    sweets_to_win: int = 29
    b: int = (int(sweets)-int(sweets_to_win))
    sweets = int(sweets) - int(b)
    ai = int(ai) + int(b)
    print('ИИ взял', b, ' конфет. У игрока сейчас', ai, ' штук. На столе осталось', sweets, ' конфет')
    print()

def win_step(*params):        # 3-е разбитие на функции ходов ИИ. Победный шаг
    global player1, ai, sweets, count_round
    b: int = sweets
    if (int(sweets) - int(b)) == 0:
        sweets = int(sweets) - int(b)
        ai = int(player1) + int(ai)
    print('ИИ забрал', b, ' конфет, на столе осталось', sweets,'! штук ИИ победил в раунде № ', count_round, ' и забрал ВСЕ конфеты!')
    print()

def AI(*params):            # Сам алгоритм ходов ИИ с учетом уровня сложности игры
    global player1, ai, sweets, count_round, difficulty, param
    if int(difficulty) == 1:
        if int(sweets) in range(1, 28):
            random.choices([win_step(param), ai_step(param)], weights=(10,  90))
        elif int(sweets) in range(30, 57):
            random.choices([danger_step(param), ai_step(param)], weights=(10, 90))
        else:
            ai_step(param)
    elif int(difficulty) == 2:
        if int(sweets) in range(1, 28):
            random.choices([win_step(param), ai_step(param)], weights=(40, 60))
        elif int(sweets) in range(30, 57):
            random.choices([danger_step(param), ai_step(param)], weights=(40, 60))
        else:
            ai_step(param)
    elif int(difficulty) == 3:
        if int(sweets) in range(1, 28):
            random.choices([win_step(param), ai_step(param)], weights=(70, 30))
        elif int(sweets) in range(30, 57):
            random.choices([danger_step(param), ai_step(param)], weights=(70, 30))
        else:
            ai_step(param)
    else:
        if int(sweets) in range(1, 28):
            random.choices([win_step(param), ai_step(param)], weights=(99, 1))
        elif int(sweets) in range(30, 57):
            random.choices([danger_step(param), ai_step(param)], weights=(99, 1))
        else:
            ai_step(param)

        param = [int(player1), int(ai), int(sweets)]
    return param

txt = 'Добро пожаловать в игру "2021 конфета!"'
for i in txt:                       # Красивые плюшки
    time.sleep(0.1)
    print(i, end='', flush=True)
print()
print()
time.sleep(2)

txt_difficulty = 'Пожалуйста выберите сложность:'

for i in txt_difficulty:           # Опять красивые плюшки)
    time.sleep(0.1)
    print(i, end='', flush=True)
print()
print('1 - Легко ')
print('2 - Нормально')
print('3 - Сложно')
print('4 - Нереально')
print()
print()


difficulty = input()
player1: int = 0
ai: int = 0
sweets: int = 100
count_round: int = 1
txt1 = 'Ходит первый игрок. Сколько хотите взять себе конфет со стола? (максимум можно взять 28 штук за 1 ход):  '
txt_correct = 'Введите корректное значение (не более 28 штук за 1 ход):  '


param = [player1, ai, sweets]

while sweets > 0:
    print('Раунд №', count_round)
    Player1(param)
    if sweets > 0:
        AI(param)
        count_round +=1
    



    
    
    