"""
Вам небхідно написати 3 класи. Мільйонери Гаражі та Автомобілі.
Звязкок наступний один мільйонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.



Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаражів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.



Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID



Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
"""

import random
import uuid
from constants import *
from termcolor import colored



class Cesar:

    def __init__(self, name, garages=0):
        self.name = name
        self.garages = []
        self.register_id = uuid.uuid4()

    def __str__(self): return f'\nname: {self.name}\ngarages: {self.garages}\nregister_id: {self.register_id}'

    def __repr__(self): return f'{vars(self)}'

    def add_garage(self, the_garage):
        if not the_garage.owner:
            vars(the_garage).update({'owner': self.register_id})
            self.garages.append(vars(the_garage))
        else:
            print('This garage already belongs to another collector.')

    def garages_count(self): return len(self.garages)

    def cars_count(self): return sum([len(garage.get('cars')) for garage in self.garages])

    def hit_hat(self):
        # return sum([int(garage.get('hit_hat_var')) for garage in self.garages])
        return sum([sum([car.price for car in garage.get('cars')]) for garage in self.garages])

    def add_car(self, car, into_garage=False):
        if not into_garage:
            max_free = max([garage.get('places') for garage in self.garages])
            if max_free:
                var_garage = [var for var, garage in enumerate(self.garages) if garage.get('places') == max_free]
                current_garage = self.garages[var_garage[0]]
                current_garage.get('cars').append(vars(car))
                current_garage.update({'places': current_garage.get('places') - 1})
            else:
                print("All place in the garages are occupied.")
        else:
            if into_garage.places > 0:
                into_garage.cars.append(car)
            else:
                print("In this garage there are no empty seats.")



    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()





class Car:

    def __init__(self, price, mileage: float, producer, type):
        self.price = price
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def __str__(self):
        return f'\nprice: {self.price}\ntype: {self.type}\nproducer: {self.producer}\nnumber: {self.number}\n' \
            f'mileage: {self.mileage}'

    def __repr__(self): return f'{vars(self)}'

    def change_car_number(self): self.number = uuid.uuid4()

    def __lt__(self, other): return self.price < other.price

    def __le__(self, other): return self.price <= other.price

    def __eq__(self, other): return self.price == other.price

    def __ne__(self, other): return self.price != other.price

    def __gt__(self, other): return self.price > other.price

    def __ge__(self, other): return self.price >= other.price



class Garage:

    def __init__(self, town, places: int, owner=None):
        self.town = town
        self.cars = []
        self.places = places
        self.owner = owner
        self.number = uuid.uuid4()



    def __str__(self): return f'\ntown: {self.town}\ncars: {self.cars}\nplaces: {self.places}\nowner: {self.owner}'

    def __repr__(self): return f'{vars(self)}'

    def add_car_into_garage(self, car):
        if self.places:
            self.cars.append(car)
        else: print("The garage is full!")
        self.places -= 1

    def remove(self, car):
        if car in self.cars: self.cars.remove(car)
        else: print("This car is not in the garage!")
        self.places += 1

    def hit_hat(self):
        return sum([car.price for car in self.cars])



# === Installation objects ===

auto1 = Car(5000, 2, random.choice(CARS_PRODUCER), random.choice(CARS_TYPES))
auto2 = Car(7000, 5, random.choice(CARS_PRODUCER), random.choice(CARS_TYPES))
auto3 = Car(10000, 7, random.choice(CARS_PRODUCER), random.choice(CARS_TYPES))

cesar1 = Cesar('Tony Stark')
cesar2 = Cesar('Ilon Mask')
cesar3 = Cesar('Vin Diesel')

garage1 = Garage(random.choice(TOWNS), 2)
garage2 = Garage(random.choice(TOWNS), 3)
garage3 = Garage(random.choice(TOWNS), 5)



# === Add auto to garage ===

print(colored(f'\n\nAdd auto1 to garage 1', 'blue'))
garage1.add_car_into_garage(auto1)
print(garage1)

print(colored(f'\n\nAdd auto2 to garage 1', 'blue'))
garage1.add_car_into_garage(auto2)
print(garage1)

print(colored(f'\n\nAdd auto3 to garage 3', 'blue'))
garage3.add_car_into_garage(auto3)
print(garage3)



# === Remove car to garage 1 ===

print(colored(f'\n\nRemove auto2 in garage 1', 'blue'))
garage1.remove(auto2)
print(garage1)



# === The sum price of all auto in the garage 1 ===

print(colored(f'\n\nThe sum price of all cars in the garage 1\n', 'blue'))
result_hit_hat = garage1.hit_hat()
print(colored('SUM : ', 'green'), result_hit_hat)



# === Add garage 1 to cesar 1 ===

print(colored(f'\n\nAdd "garage 1" to "cesar 1"\n', 'blue'))
cesar1.add_garage(garage1)
print(cesar1.garages)



# === Add garage 3 to cesar 3 ===

print(colored(f'\n\nAdd "garage 3" to "cesar 3"\n', 'blue'))
cesar3.add_garage(garage3)
print(cesar3.garages)



# === Garage Count in "cesar 1" ===

print(colored(f'\n\nGarage Count in "cesar 1"\n', 'blue'))
print(colored('Count : ', 'green'), cesar1.garages_count())



# === Garage Count in "cesar 2" ===

print(colored(f'\n\nGarage Count in "cesar 2"\n', 'blue'))
print(colored('Count : ', 'green'), cesar2.garages_count())



# === Car change number ===

print(colored(f'\n\nCar change number"\n', 'blue'))
print(colored('Before : ', 'green'), auto3.number)
auto3.change_car_number()
print(colored('After  : ', 'green'), auto3.number)



# === Car comparison ===

print(colored(f'\n\nCar comparison\n', 'blue'))

print(colored('<  : ', 'green'), auto1 <  auto2)
print(colored('<= : ', 'green'), auto1 <= auto2)
print(colored('== : ', 'green'), auto1 == auto2)
print(colored('!= : ', 'green'), auto1 != auto2)
print(colored('>  : ', 'green'), auto1 >  auto2)
print(colored('>= : ', 'green'), auto1 >= auto2)



# === Cesar comparison ===

print(colored(f'\n\nCesar comparison\n', 'blue'))
print(colored('<  : ', 'green'), cesar1 <  cesar3)
print(colored('<= : ', 'green'), cesar1 <= cesar3)
print(colored('== : ', 'green'), cesar1 == cesar3)
print(colored('!= : ', 'green'), cesar1 != cesar3)
print(colored('>  : ', 'green'), cesar1 >  cesar3)
print(colored('>= : ', 'green'), cesar1 >= cesar3)
