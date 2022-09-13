import time as tm
 
from car import Car

class World:

  # Constructor:
  def __init__(self):
  
    self.t = 0.0
    self.dt = 0.1
    self.running = True
    self.bmw = Car (" bmw " , 800.0, 600.0)
    self.tesla = Car (" tesla " , 1200.0, 600.0)
    
  def bang(self):
      while self.running:
        self.t += self.dt

        self.bmw.move(self.dt)
        self.tesla.move(self.dt)

        if self.bmw.x > 100:
          self.running = False

        if self.tesla.x > 100:
          self.running = False
    
        print(" Time: ", self.t)
        tm.sleep(self.dt)

        print("bmw", self.bmw.x)
        print("tesla", self.tesla.x)

  def stop(self):
    self.running = False
