# 1 - Crie uma classe para representar um carr. Ele deve ter um atributo que 
# diga sua potência em cavalos. Outro atributo deve dizer quanto de gasolina 
# por quilômetros ele consome. Cria duas instâncias e mostre os valores.
class CarPower:
    def __init__(self, power, range):
        self.power = power
        self.range = range

car1 = CarPower(100,200)
car2 = CarPower(200,350.5)

print("Car Power 1: ", car1.power, " horses")
print("Car range 1: ", car1.range, " Km/L")

print("Car Power 2: ", car2.power, " horses")
print("Car range 2: ", car2.range, " Km/L")

# 2 - Cria uma classe que represente uma pessoa. Ela deve possuir um name, 
# CPF e um dependente, onde o dependente é outra pessoa. 
# Dependente não é obrigatório. Crie duas instâncias: pai e filho, 
# e imprima as saídas.
class Person:
    def __init__(self, name, cpf, dependent="No dependents"):
        self.name = name
        self.cpf = cpf
        self.dependent = dependent

child = Person("Rodrigo","200.300.400-45")
father = Person("Fernando","100.200.300-34",child)

print("Name: ", child.name, " CPF: ", child.cpf, " Dependent: " , child.dependent )
print("Name: ", father.name, " CPF: ", father.cpf, " Dependent: " , father.dependent.name )

# 3 - Crie uma classe base que represente um veículo. 
# Os atributos devem ser weight do veiculo, número de rodas e potência.
# Crie uma função na classe base que diga a distância percorrida. Vamos supor que esse valor é dado pela weight do veículo
# dividido pela potência do veículo vezes mil.
# Crie os operador '>' e '<' para dizer qual veículo é mais potente. Compare um de cada tipo.
# Observação, sobrescreva os métodos __lt__ e __gt__
# Em seguida crie três classes que herdam esse veículo: ônibus, carro e moto.
# Crie uma instância de cada tipo e imprima as instâncias
class Vehicle:
    def __init__(self, weight, num_tyres, power):
        self.weight = weight
        self.num_tyres = num_tyres
        self.power = power
    def distance_travelled(self):
        return (self.power / self.weight ) * 1000
    def __lt__(self,outro) :
        return self.power < outro.power
    def __gt__(self, outro):
        return self.power > outro.power

class Bus (Vehicle):
    def __init__(self, weight, num_tyres, power):
        super().__init__(weight, num_tyres, power)

class Motorcycle (Vehicle):
    def __init__(self, weight, num_tyres, power):
        super().__init__(weight, num_tyres, power)

class Car (Vehicle):
    def __init__(self, weight, num_tyres, power):
        super().__init__(weight, num_tyres, power)

bus = Bus(1000, 6, 400)
car = Car(300, 4, 100)
motorcycle = Motorcycle(100, 2, 50)

print("Onibus, Weight: ", bus.weight, " Number of Tyres: ", bus.num_tyres, " Power: ", bus.power)
print("Car, Weight: ", car.weight, " Number of Tyres: ", car.num_tyres, " Power: ", car.power)
print("Moto, Weight: ", motorcycle.weight, " Number of Tyres: ", motorcycle.num_tyres, " Power: ", motorcycle.power)

print("Distance Travelled by the bus: ", bus.distance_travelled())
print("Distance Travelled by the car: ", car.distance_travelled())
print("Distance Travelled by the motorcycle: ", motorcycle.distance_travelled())

print(bus > car)
print(bus < motorcycle)
print(motorcycle > car)

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
    print("Object per value")
  else:
    print("Object per reference")

class Objeto:
  def __init__(self):
    pass

obj = Objeto()
value = 3

testa_objeto(obj)
testa_objeto(value)