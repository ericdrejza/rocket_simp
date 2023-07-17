import numpy as np

from coordinate_system import CoordinateSystem
from coordinate_system import CartesianCoordinateSystem


class Simulation:
  
  def __init__(self,
    rocket_components, # list of rocket components (typically, there will be just one element to start)
    coordinate_system: CoordinateSystem=CartesianCoordinateSystem, # Coordinate system to use
    time_max=100, # time that this simulation will cover (affects number of iterations)
    time_step=1 # the duration that each iteration will cover
    ) -> None:
    
    self.coordinate_system = coordinate_system
    self.rocket_components = rocket_components
    # self.simulation_log = SimulationLog()
    self.time = 0 # unit seconds
    self.time_max = time_max # unit seconds
    self.time_step = time_step # unit: seconds
  

  def update(self):
    """
    Update the objects in the simulation
    """
    self.rocket_component.update(self.time_step)


  def start(self):
    """
    Start the simulation
    """
    for time in np.arange(0, self.time_max, self.time_step):
      self.time = time
      self.update(self.time_step)



### MAIN ###
def main():
  # Define rocket component
  # rocket_component = RocketComponentHead(args)

  # Choose coordinate system
  coordinate_system = CartesianCoordinateSystem

  # Create Simulation
  # simulation = Simulation(rocket_component, coordinate_system)

  # Start simulation
  # simulation.start()



if __name__ == '__main__':
  main()
