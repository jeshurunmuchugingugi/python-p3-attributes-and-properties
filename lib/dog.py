#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name=None, breed=None):
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed
            
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value, str) and (len(value) in range(1, 26)):
            self._name = value
            print(f"good {self._name}")
        else:
            print("Name must be string between 1 and 25 characters.")
    pass
    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, value):
        if isinstance(value, str) and (value in APPROVED_BREEDS):
            self._breed = value
            print(f"good {self._breed}")
        else:
            print("Breed must be in list of approved breeds.")



dog = Dog("pug","Beagle")


