# 1 - Crie uma função que retorne a subtração de dois elementos, mas que 
# considere o valor absoluto deste valores.
func_sub = lambda x, y: abs(x) - abs(y)
print(func_sub(2, 10))

# 2 – Sem usar “ifs”, crie uma função que receba dois números e retorne a soma 
# dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser 
# sempre maior que 0.
def addiction(num1, num2):
  sum = num1 + num2
  sum = min(10000,sum)
  sum = max(0,sum)
  return sum

print(addiction(20,20))
print(addiction(5000,6000))
print(addiction(10,-20))

# 3 (DESAFIO) - Crie uma função que receba argumentos de tamanho arbitrário. 
# Todos esses argumentos serão números. Em seguida retorne o menor número 
# entre todos os recebidos.
func_min_num = lambda *x: min(*x)
print(func_min_num(1, 2, 3, 5, -1))

# 4 - Crie uma função que calcule a formula de Bhaskara, encontrado o X. 
# Os coeficientes a,b e c devem ser lidos por input.
import math
def bhaskara(a, b, c):
  """
  Calcula a fórmula de Bhaskara, encontrando o X.

  Args:
    a: Coeficiente a da equação do segundo grau.
    b: Coeficiente b da equação do segundo grau.
    c: Coeficiente c da equação do segundo grau.

  Returns:
    x: Raiz da equação do segundo grau.
  """

  delta = b ** 2 - 4 * a * c
  if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2
  else:
    return None

print(bhaskara(-2, 8, -2))

# 5 - Crie uma função que receba uma string, e para cada letra minúscula a 
# transforme em uma letra maiúscula e vice versa.
func_convert_letter = lambda string: string.swapcase()
print(func_convert_letter('HellEN is THE most beAUTiful woMan IN the WORLD'))

# 6 - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne a quantidade de vezes que essa letra tem na string. 
# Caso não ocorra nenhuma vez, retorne 0.
func_count_letter = lambda string, letra: string.lower().count(letra.lower()) if letra.lower() in string.lower() else 0
print(func_count_letter('carr', 'r'))

# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.

def find_index_caracter(text,caracter):
  index = []
  i = 0
  for char in text:
    if (char == caracter):
      index.append(i)
    i += 1
  return index

print(find_index_caracter("abcaa","a"))
print(find_index_caracter("abcab","b"))

# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e 
# também uma lista contendo todas as palavras não permitidas a serem digitadas. 
# Essa função então retornara o que foi digitado pelo usuário mas no lugar 
# das palavras não permitidas retorna o caractere '*’.

def remove_words(text, words):
  for word in words:
    if word in text:
      size_word = len(word)
      text = text.replace(word, size_word*"*")
  return text

user_text = "não pode falar a palavra droga ou diabo no chat"
forbidden_words = ['droga', 'diabo', 'chat']
print(remove_words(user_text, forbidden_words))

# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente 
# maiúscula ou totalmente minúscula.

def is_upper_or_lower(text):
  return text.islower() or text.isupper()

print(is_upper_or_lower("AAAAAAA"))

# 10 - Crie uma função que receba uma lista de textos. 
# Detecte quais os valores dessa lista são inteiros e em seguida transforme 
# eles para um número do tipo inteiro. Todos esses valores encontrados 
# serão retornados em uma nova lista que deve estar ordenada.

def transform_list(list):
  list_int = []
  for item in list:
    if item.isdecimal():
      list_int.append(int(item))
  list_int.sort()
  return list_int

list = ['12','1213r','6','8','100','3dd']

print(transform_list(list))

# 11 - Leia por input sua data de nascimento no formado Dia/Mês/Ano e 
# mostre quantos dias você já viveu.

import datetime

data_txt = input("Write your date of birth in the format day/month/year: ")
date_birth = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
calc_days_of_life = datetime.datetime.now() - date_birth
print("You have lived ", calc_days_of_life, ' days')

# 12 - Leia por input sua próxima data de aniversario no formado Dia/Mês/Ano 
# e mostre quantos dias faltam para seu próximo aniversario.

next_birthday = input("Write your next birthday in the format day/month/year:")
print("You ill have your birthday in", datetime.datetime.strptime(next_birthday, '%d/%m/%Y') - datetime.datetime.now(), ' days')