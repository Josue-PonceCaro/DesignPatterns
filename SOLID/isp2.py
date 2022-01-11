import numpy as np
from abc import ABC, abstractmethod

class Mammals(ABC):
    @abstractmethod
    def swim() -> bool:
        print("Can Swim") 

    @abstractmethod
    def walk() -> bool:
        print("Can Walk") 

class Human(Mammals):
    def swim():
        return print("Humans can swim") 

    def walk():
        return print("Humans can walk") 

class Whale(Mammals):
    def swim():
        return print("Whales can swim") 
Human.swim()
Human.walk()

Whale.swim()
Whale.walk()