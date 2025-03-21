from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass