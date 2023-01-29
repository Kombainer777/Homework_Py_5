# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите слова через "пробел: "').split()
result = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
print(result)