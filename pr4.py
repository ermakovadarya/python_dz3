# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n=int(input('Введите число'))
def to_bin(n):
    global sp
    sp=[]
    
    while n>1:
        sp.append(n-int(n/2)*2)
        n=int(n/2)
        print(n,end=' ')
    sp.append(n)
    return sp.reverse()

to_bin(n)
print(sp)