# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

def new_sp(x):
    for i in sp:
        x.append (round(i-int(i),2))

def subtraction(x):
    min=x[0]
    max=x[0]
    for i in x:
        if i<min:
            min=i
        if i>max:
            max=i
    return round(max-min,2)


sp=[round(random.uniform(0,10),2) for _ in range(10)]
res=[]
print (sp)
new_sp(res)
print(res)
print(subtraction(res))