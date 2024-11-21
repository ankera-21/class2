from datetime import datetime as dt
from datetime import timezone as tz
import math
from typing import Any

class DynamicClass:
    static_value = None
    def __init__(self):
        self.name=None

    def dynamic_attr(self,name, val): 
        setattr(self, name, val)

class ValidatedAttribute:
    
    def __init__(self) -> None:
        self._value = None
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, vale):
        if vale < 0:
            raise ValueError("Negative number ")
        self._value = vale

class Vehicle:
    vehicle_count = 0

    def __init__(self, company, model, build_year):
        self.model_name =model
        self.company = company
        self.build_year = build_year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(classification):
        return f"This is a {classification}"

class ElectricVehicle(Vehicle):
    def __init__(self, company, model, build_year):
        super().__init__(company, model, build_year)
    
    @staticmethod
    def classify_vehicle(classification):
        return f"This is an electric {classification}"

    
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
        self._diameter = None
        
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        if self._diameter is None:
            self._diameter = 2 * self._radius
        return self._diameter
    
    @radius.setter
    def radius(self, value):
        # if radius value is set we invalidate our cached _area value
        # we could make this more intelligent and see if the radius has actually changed
        # but keeping it simple
        
        # we could even add validation here, like value has to be numeric, non-negative, etc
        if value >0:
            self._radius = value
            self._diameter  = None
            self._area = None
        else:
            raise ValueError("Radius should be Non Negative")
        
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
        return self._area    
    
class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self._age = None
        self._salary = None
        self._base_salary = 50000
        self._bonus = 10

    @property
    def age(self):
        if self._age is None:
            self._age =  dt.now(tz.utc).year - self.birth_year
        return self._age

    # @property
    # def birth_year(self):
    #     return self.birth_year
    
    
    def set_birth_year(self, b_y):
        self.birth_year = b_y
        self._age=None
    

    @property
    def full_name(self):
        return self.first_name + " "+self.last_name

    @full_name.setter
    def full_name(self, name_full):
        self.first_name = name_full.split(" ")[0]
        self.last_name = name_full.split(" ")[1]
    
    @property
    def salary(self):
        if self._salary is None:
            self._salary =  self._base_salary + ((self._base_salary*self._bonus)/100)
        return self._salary
    
    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, bs):
        self._base_salary = bs
        self._salary = None
    
    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        self._bonus  = bonus
        self._salary = None

    


