from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass