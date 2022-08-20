'''Игра: компьютер угадает чиcло не более чем за 7 попыток'''


import numpy as np


    
a = 1
b = 101

number = np.random.randint(a, b)#Задаём рандомное число, которое будем искать(в диапазоне от a до b)

count = 0#Создаём переменную-счётчик, которая будет показывать количество попыток

while True:
    count+=1
    half = int((a+b) // 2)
    
    if half > number:
        b = half
    
    elif half < number:
        a = half

    else:
        print(f"Компьютер угадал число за {count} попыток. Это число {number}")
        break #конец игры выход из цикла