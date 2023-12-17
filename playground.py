#File for various types of codes

def add(*args):
    total = 0
    for n in args:
       total+= n
    
    return total

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(add(1,2,3,4,5,6))
print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
       self.make = kw.get("make")
       self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

my_car2= Car()
print(my_car2.model)
print(my_car2.make)