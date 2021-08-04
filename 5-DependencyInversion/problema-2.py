class DatabaseService:
    def getDatos(self):
        pass

class AccesoADatos:
    def __init__(self, databaseService):
        self.databaseService = databaseService

    def getDatos(self):
        self.databaseService.getDatos()

