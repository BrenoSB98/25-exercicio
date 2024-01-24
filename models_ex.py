from random import randrange

# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.
num = randrange(2, 100)
if num // 2 == 0:
    print(f'Par. The number generated is {num}')
else:
    print(f'Impar. The number generated is {num}')
    
# 2 - Da mesma forma que o exercício anterior, gere a soma de 100 números 
# aleatórios e mostre o resultado final.
sum = 0
for i in range(100):
    num = randrange(0, 10000)
    sum += num
print(sum)