# 1 - Crie uma lista com os seguintes números 1,10,6,7,8,10. 
# Em seguida printe a soma destes números.
list = []
sum = 0
for i in range(0,6):
    list.append(int(input('Write a value between 1 and 10: ')))
    sum += list[i]
print(sum)

# 2 - Cria uma list e preencha ela com valores de 1 a 100. 
# Em seguida printe esses valores.
list_2 = [ x for x in range(1, 101)]
print(list_2)

# 3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e 
# 43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores 
# repetidos entre ambas eles não podem repetir na list unida.
list_1 = []
list_2 = []
for i in range(0,7):
    list_1.append(int(input('Write a number for list 1: ')))
    list_2.append(int(input('Write a number for list 2: ')))
    
unique_list = []
for value in list_1:
    if value not in unique_list:
        unique_list.append(value)
for value in list_2:
    if value not in unique_list:
        unique_list.append(value)
    
print(sorted(unique_list))

# 4 - Crie uma list contendo todos os números negativos de -30 até -20. 
# Printe essa list.

list = [ x for x in range(-30,-19)]
print(list)

# 5 - Percorra os números de 4 a 100 e mantenha apenas aqueles divisíveis por 4.

list = [ x for x in range(4,101) if x % 4 ==0 ]
print(list)

# 6 (DESAFIO) - Crie uma list contendo todos os números de 0 a 100, mas filtre,
# mantendo apenas os números que terminam com 0.

list = [x for x in range(0,101) if str(x)[-1] == '0']
print(list)

# 7 - Percorra os números de 0 a 20 e crie um array, onde caso o número 
# terminar com zero o valor devera ser '0', caso contrario devera ser '-'.

list = [ '0' if str(x)[-1] == '0' else '-' for x in range(0,21)] 
print(list)