# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:54:26 2019

@author: rajar
"""

from abc import ABC, abstractmethod

class Employee:
    @abstractmethod
    
    def calculate_salary(self, sal):
        pass
    
class Developer(Employee):
    
    def calculate_salary(self, sal):
        finalsalary = sal * 1.10
        return finalsalary
    
emp_1 = Developer()
print(emp_1.calculate_salary(10000))
