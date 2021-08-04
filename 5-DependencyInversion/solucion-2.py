from abc import ABC, abstractmethod

#quiero agregar o cambiar el servicio de base de datos por una api o similar

class Conexion(ABC):

    @abstractmethod
    def getDatos(self):
        pass

    @abstractmethod
    def setDatos(self):
        pass

class AccesoADatos:
    def __init__(self, conexion):
        self.conexion = conexion

    def getDatos(self):
        self.conexion.getDatos()


class DatabaseService(Conexion):
    def getDatos(self):
        pass

    def setDatos(self):
        pass


class APIService(Conexion):
    def getDatos(self):
        pass

    def setDatos(self):
        pass
