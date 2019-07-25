#!/usr/bin/env python
# -*-coding:utf-8 -*-

from src.model import Dog

d = Dog("D", 14)
d.sit()


class Car(object):
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.dosomething_reading = 0

    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_dosomething_reading(self):
        print("This car has " + str(self.dosomething_reading) + "miles on it.")

    def update_dosomething_reading(self, mileage):
        if mileage >= self.dosomething_reading:
            self.dosomething_reading = mileage
        else:
            print("You can't roll  back an odometer!")

    def increment_dosomething(self, miles):
        self.dosomething_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """调用父类"""
        super(ElectricCar, self).__init__(make, model, year)

    """重写"""
    def get_descriptive(self):
        long_name = self.make + " " + self.model
        return long_name.title()


if __name__ == '__main__':
    my_car = ElectricCar("testla", "models", 2016)
    print(my_car.get_descriptive())
