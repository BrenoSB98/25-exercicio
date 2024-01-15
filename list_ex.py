# 1 - Crie uma lista com os seguintes números 1,10,6,7,8,10. 
# Em seguida printe a soma destes números.

lista = []
soma = 0
for i in range(0,6):
    lista.append(int(input('Digite um valor entre 1 e 10: ')))
    soma += lista[i]
print(soma)

# 2 - Cria uma lista e preencha ela com valores de 1 a 100. 
# Em seguida printe esses valores.
lista_2 = [ x for x in range(1, 101)]
print(lista_2)

# 3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e 
# 43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores 
# repetidos entre ambas eles não podem repetir na lista unida.
lista_1 = []
lista_2 = []
for i in range(0,7):
    lista_1.append(int(input('Digite um número para lista 1: ')))
    lista_2.append(int(input('Digite um número para lista 2: ')))
    
lista_unica = []
for valor in lista_1:
    if valor not in lista_unica:
        lista_unica.append(valor)
for valor in lista_2:
    if valor not in lista_unica:
        lista_unica.append(valor)
    
print(sorted(lista_unica))

# 4 - Crie uma lista contendo todos os números negativos de -30 até -20. 
# Printe essa lista.

lista = [ x for x in range(-30,-19)]
print(lista)

# 5 - Percorra os números de 4 a 100 e mantenha apenas aqueles divisíveis por 4.

lista = [ x for x in range(4,101) if x % 4 ==0 ]
print(lista)

# 6 (DESAFIO) - Crie uma lista contendo todos os números de 0 a 100, mas filtre,
# mantendo apenas os números que terminam com 0.

lista = [x for x in range(0,101) if str(x)[-1] == '0']
print(lista)

# 7 - Percorra os números de 0 a 20 e crie um array, onde caso o número 
# terminar com zero o valor devera ser '0', caso contrario devera ser '-'.

lista = [ '0' if str(x)[-1] == '0' else '-' for x in range(0,21)] 
print(lista)