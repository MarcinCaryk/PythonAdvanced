import numpy as np
from abc import ABC, abstractmethod

class Operations(ABC):
    '''Operations'''
    @abstractmethod
    def operation(self):
        pass

class Mean(Operations):
    '''Max'''
    def operation(lst):
        print(f"The mean is {np.mean(lst)}")

class Max(Operations):
    '''Max'''
    def operation(lst):
        print(f"The max is {np.max(lst)}")

class Sum(Operations):
    def operation(lst):
        print(f"The sum is {np.sum(lst)}")

class Mult(Operations):
    def operation(lst):
        m=1
        for i in lst:
            m = m*i
        print(f"The subs is {m}")



class Main:
    '''Main'''
    @abstractmethod
    def get_operations(lst):
        # __subclasses__ will found all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(lst)


if __name__ == "__main__":
    Main.get_operations([1,2,3,4,5])