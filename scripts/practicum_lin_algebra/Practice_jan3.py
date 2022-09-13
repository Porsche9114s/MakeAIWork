class Vector:
    """
    this is a class to generate vectors
    """
    def __init__(self, scalarlist):
        self.scalarlist = scalarlist

    def addVector(self, otherVector):
            pass

    def multplyVector(self, otherVector):
            pass

    def printVector(self):
            print(f"dit is de vector: {self.scalarlist}")
        
list = [9,8]
v = Vector(list)
v.printVector()

        