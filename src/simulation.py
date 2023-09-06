from logging import Logger
import numpy as np

import pandas as pd

from rocket_component import RocketComponent, HeadRocketComponent


# Set up logger
sim_logger = Logger('simulation')

class Simulation:
  
  def __init__(self,
    rocket_component: RocketComponent, time_max=100, time_step=1
    ) -> None:
    """
    Initializes simulation

    Parameters:
      rocket_component: RocketComponent
        RocketComponent object that
      time_max: float
        Max time of simulation, defaults to 100
      time_step: float
        Amount of time to past each iteration of the simulation
    """
    
    self.rocket_components = [rocket_component]
    # self.simulation_log = SimulationLog()
    self.time = 0 # unit seconds
    self.time_max = time_max # unit seconds
    self.time_step = time_step # unit: seconds
  

  def log_rockets(self) -> None:
    list(map(lambda rocket_component: rocket_component.log(self.time),
      self.rocket_components))


  def print_rocket_components(self):
    for rocket_component in self.rocket_components:
      print(f'{self.time}: {rocket_component.string_info()}')


  def run(self) -> None:
    """
    Start the simulation
    """
    # Create initial rows for each rocket component's log
    self.log_rockets()
    self.print_rocket_components()

    # Loop through times
    for time in np.arange((self.time + self.time_step),
      (self.time_max + self.time_step), self.time_step):
      self.time = time
      self.update()

      for rocket_component in self.rocket_components:
        rocket_component.output_log()
      
      self.print_rocket_components()


  def update(self) -> None:
    """
    Update the objects in the simulation
    """
    # Call update function on each RocketComponent
    list(map(lambda rocket_component:
      rocket_component.update(self.time, self.time_step),
      self.rocket_components))


### MAIN ###
def main():
  # Build rocket component
  head_rocket_component = HeadRocketComponent(0)
  
  # Create simulation
  simulation = Simulation(head_rocket_component, time_max=100)

  # Start simulation
  simulation.run()
  return



if __name__ == '__main__':
  main()
