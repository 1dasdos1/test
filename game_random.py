import random as rnd
# Загадали случайное число
lb = 1
rb = 100
x = rnd.randint(1, 100)
n = 4
print('Я загaдал число от %s до %s. У тебя %s попыток' %(lb, rb, n))

for g in range(n):
    y = int(input('Назови число: '))
    if x == y:
         print('You Win!')
         break
    elif x > y:
        print('Моё число больше твоего')
    elif x < y:
        print('Моё число меньше твоего')
else:
    print('Game Over. My namber: %s' %(x))