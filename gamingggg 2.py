#Gaming mäng
#IT21
#24.03.2022


from random import randint
import time

enemy = 100
fighter = 100
php = randint(4,34)
shp = randint(1,37)
khp = randint(6,31)

'''
gender = input("Vali sugu(M,N,Muu): ")
user = input("Vali oma lemmik taguja (1. Prill Peedu \n 2. Isand Sten \n 3. Koristaja Kaspar): ")
'''
players = {'peedu': [100, 34]}
print(players["peedu"][0])


while enemy > 1:
    enemy -= randint(10,players["peedu"][1])
    print(enemy)
    