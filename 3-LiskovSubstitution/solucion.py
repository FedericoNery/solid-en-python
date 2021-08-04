class Bird:
    def eat(self):
        pass

class Ostrich(Bird):
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Duck (FlyingBird):
    pass

if __name__ == '__main__':
    birdList = list()
    birdList.append(Bird())
    birdList.add(Ostrich())
    birdList.add(Duck())
    birdList.add(FlyingBird())

    # Let the birds eat
    for bird in birdList:
        bird.eat()

    flyingBirdList = list();
    flyingBirdList.append(Duck())
    flyingBirdList.append(FlyingBird())

    #Let the flying birds fly
    for bird in flyingBirdList:
        bird.fly()


"""
Ostrich no vuela, no está soportado

Según el "Liskov Substitution Principle" deberíamos poder utilizar las clases Duck y/o Ostrich en lugar de la superclase Bird. 
Debido a que no se cumple este principio no se puede usar de forma indistinta la superclase o las subclases sin generar errores en 
la aplicación ya que la subclase Ostrich tiene unas restricciones superiores a la superclase en el método fly(). Este método lanza una 
excepción de tipo 'UnsupportedOperationException' que no se lanza ni en la otra subclase ni en la superclase. 
Por tanto no se pueden usar de forma indistinta. Si usamos la subclase Ostrich deberemos capturar o relanzar dicha excepción.

Para cumplir con el "Liskov Substitution Principle" refactorizamos la superclase Bird y creamos la clase FlyingBird que hereda de la clase Bird. 
Movemos el método fly() a la subclase correspondiente y la clase Duck ahora hereda de la clase FlyingBrid. De esta forma 
podremos usar las subclases y la superclase de forma indistinta.

Podremos usar el método fly() independientemente de que tengamos un objeto de tipo Duck o FlyingBird y podremos usar el
método eat() independientemente de que tengamos un objeto de tipo Bird, Ostrich, Duck o FlyingBird.

"""