from abc import ABC, abstractmethod
import numpy as np

class specification(ABC):
    @abstractmethod
    def operation(listVal_):
        pass

class meanList(specification):
    def operation(listVal_):
        print(np.mean(listVal_))

class maxList(specification):
    def operation(listVal_):
        print(max(listVal_))

class statistics:
    @abstractmethod
    def statisticsRequirements(listVal_):
        for operator in specification.__subclasses__():
            operator.operation(listVal_)



if __name__ == '__main__':
    values = [1,2,3,4,5]

    statistics.statisticsRequirements(values)
