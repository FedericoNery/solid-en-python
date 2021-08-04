from abc import ABC, abstractmethod
class IAve(ABC):

    @abstractmethod
    def comer(self):
        pass

class IAveVoladora(ABC):
    @abstractmethod
    def volar(self):
        pass


class IAveNadadora(ABC):
    def nadar(self):
        pass

class Loro(IAve, IAveVoladora):
    def volar(self):
        pass

    def comer(self):
        pass

class Pinguino (IAve, IAveNadadora):

    def nadar(self):
        pass

    def comer(self):
        pass