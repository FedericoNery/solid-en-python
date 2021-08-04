from abc import ABC, abstractmethod

class IAve(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Loro (IAve):
    def volar(self):
        pass

    def comer(self):
        pass

class Tucan (IAve):
    def volar(self):
        pass

    def comer(self):
        pass

#--------------------------
class IAve(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def nadar(self):
        pass

class Loro (IAve):
    def volar(self):
        pass

    def comer(self):
        pass

    def nadar(self):
        pass


class Pinguino (IAve):

    def volar(self):
        pass

    def comer(self):
        pass

    def nadar(self):
        pass