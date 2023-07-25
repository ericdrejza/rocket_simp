import numpy as np
import math


class Simulation:

  def __init__(self,
    rocket_components, # list of rocket components (typically, there will be just one element to start)
    time_max=100, # time that this simulation will cover (affects number of iterations)
    time_step=1 # the duration that each iteration will cover
    ) -> None:

    self.rocket_components = rocket_components
    # self.simulation_log = SimulationLog()

    # Initial Conditions:
    self.x = 0  # m
    self.y = 0  # m
    self.v = 0  # m/s
    self.l = 70  # m
    self.w = 4  # m
    self.alpha = math.pi / 2  # radians
    self.time = 0 # unit seconds
    self.time_max = time_max # unit seconds
    self.time_step = time_step # unit: seconds
  

  def update(self):
    """
    Update the objects in the simulation
    """

    for rocket_component in self.rocket_components:
      rocket_component.update(self.time_step)


  def start(self):
    """
    Start the simulation
    """

    for time in np.arange(0, self.time_max, self.time_step):
      self.time = time
      self.update()



### MAIN ###
def main():
  # Define rocket component
  # rocket_component = RocketComponentHead(args)

  # Create Simulation
  # simulation = Simulation(rocket_component, coordinate_system)

  # Start simulation
  # simulation.start()



if __name__ == '__main__':
  main()
