

class Track:

    def __init__(self, distance):

        self.distance = distance

        #list of cars
        self.cars = []


    def addCars(self, car):

        self.cars.append(car)

    def step(self, dt):

        for car in self.cars:

            x, v = car.step(dt)

            #stop simulation when the car has reached end of track

            if x > self.distance:

                print("we have a Winner", car, name)

                return False

        return True


