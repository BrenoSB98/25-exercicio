# 1 - Crie uma classe para representar um carro. Ele deve ter um atributo que 
# diga sua potência em cavalos. Outro atributo deve dizer quanto de gasolina 
# por quilômetros ele consome. Cria duas instâncias e mostre os valores.
class CarroPotencia:
    def __init__(self, potencia, alcance):
        self.potencia = potencia
        self.alcance = alcance

carro1 = CarroPotencia(100,200)
carro2 = CarroPotencia(200,350.5)

print("Potência do carro 1: ", carro1.potencia, " cavalos")
print("Alcance do carro 1: ", carro1.alcance, " Km/l")

print("Potência do carro 2: ", carro2.potencia, " cavalos")
print("Alcance do carro 2: ", carro2.alcance, " Km/l")

# 2 - Cria uma classe que represente uma pessoa. Ela deve possuir um nome, 
# CPF e um dependente, onde o dependente é outra pessoa. 
# Dependente não é obrigatório. Crie duas instâncias: pai e filho, 
# e imprima as saídas.
class Pessoa:
    def __init__(self, nome, cpf, dependente="Sem Dependentes"):
        self.nome = nome
        self.cpf = cpf
        self.dependente = dependente

filho = Pessoa("Rodrigo","200.300.400-45")
pai = Pessoa("Fernando","100.200.300-34",filho)

print("Nome: ", filho.nome, " CPF: ", filho.cpf, " Dependente: " , filho.dependente )
print("Nome: ", pai.nome, " CPF: ", pai.cpf, " Dependente: " , pai.dependente.nome )

# 3 - Crie uma classe base que represente um veículo. 
# Os atributos devem ser peso do veiculo, número de rodas e potência.
# Crie uma função na classe base que diga a distância percorrida. Vamos supor que esse valor é dado pela peso do veículo
# dividido pela potência do veículo vezes mil.
# Crie os operador '>' e '<' para dizer qual veículo é mais potente. Compare um de cada tipo.
# Observação, sobrescreva os métodos __lt__ e __gt__
# Em seguida crie três classes que herdam esse veículo: ônibus, carro e moto.
# Crie uma instância de cada tipo e imprima as instâncias
class Veiculo:
    def __init__(self, peso, num_rodas, potencia):
        self.peso = peso
        self.num_rodas = num_rodas
        self.potencia = potencia
    def distancia_percorrida(self):
        return (self.potencia / self.peso ) * 1000
    def __lt__(self,outro) :
        return self.potencia < outro.potencia
    def __gt__(self, outro):
        return self.potencia > outro.potencia

class Onibus (Veiculo):
    def __init__(self, peso, num_rodas, potencia):
        super().__init__(peso, num_rodas, potencia)

class Moto (Veiculo):
    def __init__(self, peso, num_rodas, potencia):
        super().__init__(peso, num_rodas, potencia)

class Carro (Veiculo):
    def __init__(self, peso, num_rodas, potencia):
        super().__init__(peso, num_rodas, potencia)

onibus = Onibus(1000, 6, 400)
carro = Carro(300, 4, 100)
moto = Moto(100, 2, 50)

print("Onibus, Peso: ", onibus.peso, " Número de Rodas: ", onibus.num_rodas, " Potência: ", onibus.potencia)
print("Carro, Peso: ", carro.peso, " Número de Rodas: ", carro.num_rodas, " Potência: ", carro.potencia)
print("Moto, Peso: ", moto.peso, " Número de Rodas: ", moto.num_rodas, " Potência: ", moto.potencia)

print("Distancia Percorrida do onibus: ", onibus.distancia_percorrida())
print("Distancia Percorrida do carro: ", carro.distancia_percorrida())
print("Distancia Percorrida da moto: ", moto.distancia_percorrida())

print(onibus > carro)
print(onibus < moto)
print(moto > carro)

# 4 - Cria uma classe que represente um número negativo, 
# use propriedades (@property)  para controlar o valor guardado pela classe, 
# sem deixar que ele fique positivo (0 pode). Além disso crie alguns operadores 
# para comparação e de subtração. Cuide para que nenhum valor positivo surja.
class NegativeNumber:
    def __init__(self, number):
        self.__number=0
        self.number = number
    @property
    def get_number(self):
        return self.number
    @get_number.setter
    def set_number(self, value):
        if value <= 0:
            self.__number = value
    def __lt__(self, other_value):
        return self.__number < other_value.__number
    def __gt__(self, other_value):
        return self.__number > other_value.__number
    def __sub__ (self, other_value):
        result = self.__number - other_value.__number
        if result > 0:
            result = 0
        return result

num1 = NegativeNumber(-10)
num2 = NegativeNumber(-20)
num3 = NegativeNumber(10)

print(num1.number, num2.number, num3.number)
print(num1 > num2)
print(num1 - num2)

# 5 - Crie uma função  que diga se um objeto é um primitivo 
# do Python, informando que é sempre passado valor Ex: [int, float, str, bool], 
# ou se é um objeto passado por referência

def testa_objeto(obj):
  if isinstance(obj, (int, float, str, bool)):
    print("Objeto por valor")
  else:
    print("Objeto por referência")

class Objeto:
  def __init__(self):
    pass

obj = Objeto()
valor = 3

testa_objeto(obj)
testa_objeto(valor)