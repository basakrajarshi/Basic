# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:47:59 2019

@author: rajar
"""

class Animal:
    def __init__(self, name):
        self.name = name
        def talk(self):
            pass
        
class Dog(Animal):
    def talk(self):
        print('woof')
        
class Cat(Animal):
    def talk(self):
        print('MEOW!')
        
c = Cat('kitty')
c.talk()
d = Dog(Animal)
d.talk()
