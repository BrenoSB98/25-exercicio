# 1 - Crie uma função chamada “e_negativo” que receba um número,  
# retorna um booleano “True” se o número for negativo, 
# caso contrário retorna “False”.

def e_negativo(num):
    return num < 0

print(e_negativo(2))
print(e_negativo(-2))


# 2 - Crie um função que receba um array de números (int ou float) 
# e retorne sua soma.
def soma_vetor(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(soma_vetor([10, 20, 30]))

# 3 - Crie um função que receba uma string e que conte e retorne o número 
# de vogais desta string.
def conta_vogal(string):
    count = 0
    for i in string:
        if i in "aeiou":
            count += 1
    return count

print(conta_vogal('areio'))

# 4 - Crie um função que retorne o último caractere de um string recebida.
def ultimo_caracter(string):
    return string[-1]

print(ultimo_caracter('areio'))

# 5 - Crie um função que receba dois números e uma string dizendo se deve 
# realizar a soma ou subtração do números.
def calculadora(x, y, string):
    if string == '-':
        return x - y
    elif string == '+':
        return x + y
    else:
        print('Opção Inválida!! Escolha entre o sinal de + ou -!!')
        
        
print(calculadora(2, 2, '+'))
print(calculadora(2, 2, '-'))
calculadora(2, 2, '*')

# 6 - Crie um função que receba uma lista de elementos e um valor qualquer. 
# Em seguida retorne um booleano dizendo se o valor foi encontrado 
# ou não na lista.
def encontra_valor(arr, valor):
    for i in arr:
        if i == valor:
            return True
        return False
    
print(encontra_valor([10, 20, 30], 40))

# 7 - Crie um função que receba uma lista de elementos e um valor qualquer.  
# Em seguida retorne um booleano dizendo se o valor foi encontrado ou não 
# e também a posição onde foi encontrado.
def encontra_valor_e_indice(arr, valor):
    for i in range(len(arr)):
        if arr[i] == valor:
            return True, i+1
    return False, -1

print(encontra_valor_e_indice([10, 20, 30], 30))

# 8 - Crie uma função que recebe um número arbitrário de parâmetros. 
# Em seguida diga qual o tipo de cada parâmetro
def tipo_parametro(*args):
    for i in args:
        print(type(i))

tipo_parametro(10, 2.2, 'f', 1)

# 9 - Crie uma função que receba um string, mas que possua um decorator para 
# transforma-la em uma citação, ou seja você deve retornar strings entre 
# aspas duplas, além disso transforme todos os caracteres para minúscula 
# usando a função lower().
def citacao(func):
  def func_inner(str):
    return '"' + func(str).lower() + '"'
  return func_inner

@citacao
def tranforma(str):
  return str

print("E disse Charlie Brown Jr: ", tranforma("Só os loucos sabem!"))

# 10 - Cria uma função recursiva que itere os números de 0 até 10 e printe o 
# resultado de sua divisão inteira com o número três.
def print_div_3(num):
  if num ==11:
    return
  print(num // 3)
  print_div_3(num+1)

print_div_3(0)