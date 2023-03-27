
# Задача 1
# class Auto:
#     def __init__(self, brand, age, marka, color=None, mass=None):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.marka = marka
#         self.mass = mass
#
#     def move(self):
#         print("move")
#     def stop(self):
#         print("stop")
#     def birthday(self):
#         self.age += 1
#
# auto = Auto("Toyota", 10, "Corolla", "black", 1750)
# auto.birthday()
# auto.move()
# auto.stop()

# Задача 2
# import time
# class Truck(Auto):
#     def __init__(self, brand, age, marka, max_load, color=None, mass=None):
#         super().__init__(brand, age, marka, color=None, mass=None)
#         self.max_load = max_load
#     def move(self):
#         print("attention")
#         super().move()
#     def load(self):
#         time.sleep(1)
#         print("load")
#         time.sleep(1)
#
# truck_1 = Truck("DAF", 10, "XF", 40000, "blue", 7000)
# truck_2 = Truck("Mercedes", 8, "Actros", 42000, "green", 9000)
# truck_1.move()
# truck_1.load()
# truck_2.move()
# truck_2.load()
#
# class Car(Auto):
#     def __init__(self, brand, age, marka, max_speed, color=None, mass=None):
#         super().__init__(brand, age, marka, color=None, mass=None)
#         self.max_speed = max_speed
#     def move(self):
#         super().move()
#         print(f"max_speed is {self.max_speed}")
#
# car_1 = Car("Audi", 20, "100", 120, "red", 2100)
# car_2 = Car("Porshe", 6, "Cayen", 210, "grey", 2500)
#
# car_1.move()
# car_2.move()

