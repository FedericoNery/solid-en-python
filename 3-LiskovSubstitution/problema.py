class Bird:
    def fly(self):
        pass
    def eat(self):
        pass

class Duck(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        pass
        #throw new UnsupportedOperationException()


if __name__ == '__main__':
    birdList = list()
    birdList.add(Bird())
    birdList.add(Duck())
    birdList.add(Ostrich())

    # Let the birds fly
    for bird in birdList:
        bird.fly()


