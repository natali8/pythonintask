﻿# Задача 5. Вариант 8.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из семи дней недели.

# Nikolaev N.A.
# 01.04.2016
# Понедельник, Вторник, Среда, Четверг, Пятница ,Суббота, Воскресенье
import random
x=random.choice(["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"])
print ("Программа случайным образом отображает название одного из семи дней недели.")
print (x)

input("\n\nНажмите Enter для выхода.")
