# 1 - Crie uma função iterável “meses” que retorne meses. 
# Use um laço for para mostrar os valores.
def returnMonth():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for i in months:
        yield i

for month in returnMonth():
  print(month)
  
# 2 - Cria uma função iterável que receba uma lista de números e que retorne 
# a cada iteração um item dessa lista multiplicado por dois.
def doubleReturn(list):
    for i in list:
        yield i * 2

list = [1,2,3,4,5]

for element in doubleReturn(list):
  print(element)
  
# 3 - Crie uma classe iterável chamada “Tabuada” que calcule a tabuada da 
# multiplicação do número recebido no construtor. 
# A cada iteração ela deve retornar um resultado da tabuada. 
# Para testar use um laço for.
class MultiplicationTable:
    def __init__(self, x):
       self.x = x
    
    def __iter__(self):
        self.actual = 0
        return self
    
    def __next__(self):
        self.actual += 1
        if self.actual == 11:
            raise StopIteration
        return self.actual * self.x

multiplication_table = MultiplicationTable(2)

for i in multiplication_table:
  print(i)