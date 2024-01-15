# 1 - Crie uma função que retorne a subtração de dois elementos, mas que 
# considere o valor absoluto deste valores.
func_sub = lambda x, y: abs(x) - abs(y)
print(func_sub(2, 10))

# 2 – Sem usar “ifs”, crie uma função que receba dois números e retorne a soma 
# dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser 
# sempre maior que 0.
def soma(num1,num2):
  soma = num1 + num2
  soma = min(10000,soma)
  soma = max(0,soma)
  return soma

print(soma(20,20))
print(soma(5000,6000))
print(soma(10,-20))

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
func_converte_letra = lambda string: string.swapcase()
print(func_converte_letra('Hellen É a MAis GOstosa dO MUndo'))

# 6 - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne a quantidade de vezes que essa letra tem na string. 
# Caso não ocorra nenhuma vez, retorne 0.
func_count_letra = lambda string, letra: string.lower().count(letra.lower()) if letra.lower() in string.lower() else 0

print(func_count_letra('carro', 'r'))

# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.

def encontra_ocorrencias(texto,caracter):
  indices = []
  indice =0
  for char in texto:
    if (char == caracter):
      indices.append(indice)
    indice += 1
  return indices

print(encontra_ocorrencias("abcaa","a"))
print(encontra_ocorrencias("abcab","b"))

# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e 
# também uma lista contendo todas as palavras não permitidas a serem digitadas. 
# Essa função então retornara o que foi digitado pelo usuário mas no lugar 
# das palavras não permitidas retorna o caractere '*’.

def retira_palavras(texto, palavras):
  for palavra in palavras:
    if palavra in texto:
      texto = texto.replace(palavra,"*")
  return texto

texto_usuario = "não pode falar a palavra droga ou diabo no chat"
palavras_proibidas = ['droga','diabo']
print(retira_palavras(texto_usuario,palavras_proibidas))

# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente 
# maiúscula ou totalmente minúscula.

def e_maiscula_ou_minuscula(texto):
  return texto.islower() or texto.isupper()

print(e_maiscula_ou_minuscula("AAAAAAA"))

# 10 - Crie uma função que receba uma lista de textos. 
# Detecte quais os valores dessa lista são inteiros e em seguida transforme 
# eles para um número do tipo inteiro. Todos esses valores encontrados 
# serão retornados em uma nova lista que deve estar ordenada.

def transforma_lista(lista):
  lista_inteiros = []
  for item in lista:
    if item.isdecimal():
      lista_inteiros.append(int(item))
  lista_inteiros.sort()
  return lista_inteiros

lista = ['12','1213r','6','8','100','3dd']

print(transforma_lista(lista))

# 11 - Leia por input sua data de nascimento no formado Dia/Mês/Ano e 
# mostre quantos dias você já viveu.

import datetime

data_txt = input("Digite a data em que você nasceu em formato dia/mês/ano: ")
data_nascimento = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_agora - data_nascimento
print("Você já vivieu ", diferenca_datas, ' dias')

# 12 - Leia por input sua próxima data de aniversario no formado Dia/Mês/Ano 
# e mostre quantos dias faltam para seu próximo aniversario.

data_proximo = input("Digite a data do seu próximo aniversário no formato dia/mes/ano")
data_aniversario = datetime.datetime.strptime(data_proximo, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_aniversario - data_agora
print("Você fará aniversário daqui ", diferenca_datas.days , ' dias')