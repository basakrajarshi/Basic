# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:37:00 2019

@author: rajar
"""

class employee:
    #perc_raise = 1.05
    def __init__(self, first, last, sal):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.email = first+ '.' + last + '@company.com'
        self.perc_raise = 1.05
        
    def fullname(self):
        return '{}{}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amount)
        
class developer(employee):
    raise_amount = 1.04
    def __init__(self, first, last, sal, prog_lang):
        super().__init__(first, last, sal)
        self.prog_lang = prog_lang
        
        
#emp_1 = employee('aayushi', 'johari', 350000)
#emp_2 = employee('test', 'test', 100000)
#print(emp_1.email)
#print(emp_2.email)
#print(emp_1.fullname())
#print(emp_2.fullname())
#print(emp_1.sal)
#emp_1.apply_raise()
#print(emp_1.sal)
emp_1 = developer('aayushi', 'johari', 100000, 'python')
print(emp_1.email)
print(emp_1.raise_amount)
print(emp_1.prog_lang)
