# Задача 1 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def summa(sum):
    for i in range(1,len(sp),2):
        sum+=sp[i]
    return sum

sp=[random.randint(0,10) for _ in range(10)]
sum=0
print (sp)
print(summa(sum))