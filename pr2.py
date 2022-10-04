# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

def exponent(x):
    if len(sp)%2==0:
        for i in range(0,int(len(sp)/2)):
            x.append(sp[i]*sp[len(sp)-1-i])
    else:
        for i in range(0,int(len(sp)/2)+1):
            x.append(sp[i]*sp[len(sp)-1-i])
        
sp=[random.randint(0,10) for _ in range(9)]
res=[]
print (sp)
exponent(res)
print(res)