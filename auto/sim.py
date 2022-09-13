# from file import class
from world import World

from track import Track

# created instance of World class
world = World()

world.bang()

#create new track instance
track = Track(100)
 
#Create a tesla
tesla = Car("tesla", 600, 800)

#create a bmw
bmw = Car("bmw", 1200, 900)

track.addCar(tesla)
track.addCar(bmw)

#add track to the world
world.addtrack(track)

#start the simulation

