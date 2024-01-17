import numpy as np
# 1.Crie um array com os números de 0 a 9, utilize somente 1 dimensão.
print(np.arange(10))

# 2.Crie um array com os números de 0 a 9 como o exercício anterior, 
# mas utilize List Compreensions.
print(np.array([i for i in range(10)]))

# 3.Crie um array com os números de 0 a 8, utilize 2 dimensões, ou seja, 
# com 3 linhas (3x3)
print(np.arange(9).reshape((3,3)))

# 4.Crie um array do tipo float, com 10 número de sua escolha, 
# mas utilize 32 bits/4 bytes.
print(np.float32([i for i in range(10)]))
print(np.arange(10, dtype='f4'))

# 5.Crie um array com os números de 1 a 20, escolhendo o tipo de dado que 
# ocupara o menor espaço da memoria. Em seguida imprima o quanto 
# ele ocupou em bytes.
print(np.int8([i for i in range(1, 21)]))
print(np.arange(1, 21, dtype=np.int8))

# 6.Crie uma matriz 2x2 e imprima o primeiro elemento da primeira linha, 
# e o último elemento da última linha.
array = np.random.randint(1, 10,(2, 2))
print(array)
for i in range(len(array)):
    for j in range(len(array)):
        if i == j:
            print(array[i, j])

# 7.Gere uma array 3x3 com números inteiros aleatórios entre 5 e 20. 
# Então imprima a primeira coluna e última linha
array = np.random.randint(5, 25,(3, 3))
print(array)
for i in range(len(array)):
    for j in range(len(array)):
        if j == 0 or i == 2:
            print(array[i, j])
print(array[:,0])
print(array[2,:])

# 8. Crie uma matriz 3x3 aleatória. Percorra linha por linha com um laço e 
# imprima a soma de cada linha.
array = np.random.randint(1, 50,(3, 3))
print(array)
for linha in array:
    print(np.sum(linha))

# 9.Gere um array com os valores pares de 0 a 100 com list comprehension.
print(np.array([i for i in range(0, 101) if i % 2 == 0]))

# 10.Crie uma array 4x9 com valores quaisquer, redimensione para as 
# dimensões 36, e 6x6
array = np.random.randint(1, 100, (4,9))
print(array)
print(array.reshape(36))
print(array.reshape(6,6))

# 11. Crie uma função que receba três arrays de mesmo formato, então retorne 
# elas concatenadas em uma só. Se as matrizes recebidas não forem do 
# mesmo formato gere uma exceção.
def combineArray(arr1, arr2, arr3):
    if arr1.shape != arr2.shape or arr1.shape != arr3.shape or arr3.shape != arr2.shape:
        raise Exception('O formato dos arraay são diferentes')
    return np.concatenate((arr1, arr2, arr3))

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.array([7,8,9])
print()
print(combineArray(array1, array2, array3))

# 12.Crie uma função que divida um array em N pedaços, mas mantenha so os 
# valores absolutos dos valores deste array.
def divide_abs(arr, n):
    arr = np.array_split(arr,n)
    return np.abs(arr)

array1 = np.array([1,2,3,-4,5,-7])
print()
print(divide_abs(array1,2))

# 13.Crie uma função que receba um array e retorne quantos números positivos ela 
# contêm.
def count_positives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count

array = np.array([1,2,3,4,5,-7])
print()
print(count_positives(array))

def count_positive(arr):
  return len(np.where(arr>0)[0])

array = np.array([1,2,3,4,5,-7])
print()
print(count_positives(array))

#14.Crie uma função que receba uma matriz e retorne os índices dos números que 
# são divisíveis por 3.
divide_for_three = lambda arr : np.where(arr % 3 == 0)[0]

array = np.array([4,5,6,7,8,9])
print()
print(divide_for_three(array))

# 15.Crie uma função que diga se um array possui números negativos
has_negative_number = lambda arr: np.any(arr < 0)

array = np.array([4,5,6,7,8,-9])
print()
print(has_negative_number(array))

# 16.Crie uma função que remova os números negativos de uma array.
def remove_negative_numbers(arr):
    filter = arr >= 0
    return arr[filter]

array = np.array([1,-5,5,4,3,-2,-1])
print()
print(remove_negative_numbers(array))

# 17.Crie uma função que receba um número inicial e final, e uma array. 
# A função deve retornar uma nova array somente com os números 
# dentro deste intervalo.
def remove_values(arr, inicial, final):
  filter = (arr >= inicial) & (arr <= final)
  return arr[filter]

array = np.array([i for i in range(-10,11)])
print()
print(array)
print(remove_values(array,0,7))

# 18.Crie uma função que ordene uma matriz e remova todos os números impares.
def order_par(arr):
  arr = np.sort(arr)
  filter = arr % 2 != 0
  return arr[filter]

array = np.random.randint(0,10,(100))
print()
print(order_par(array))

# 19.Realize o mesmo exercício anterior, mas remova valores duplicados.
def order_par_uniques(arr):
  arr = np.sort(arr)
  filter = arr % 2 != 0
  return np.unique(arr[filter])

array = np.random.randint(0,10,(100))
print()
print(order_par_uniques(array))
