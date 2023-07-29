from logging import Logger
import numpy as np

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
    map(lambda rocket_component: rocket_component.log(self.time),
      self.rocket_components)


  def update(self) -> None:
    """
    Update the objects in the simulation
    """
    # Call update function on each RocketComponent
    map(lambda rocket_component:
      rocket_component.update(self.time, self.time_step, log=True),
      self.rocket_components)


  def start(self) -> None:
    """
    Start the simulation
    """
    # Create initial rows for each rocket component's log
    self.log_rockets()

    # Loop through times
    for time in np.arange((self.time + self.time_step), (self.time_max + self.time_step), self.time_step):
      self.time = time
      self.update()
      



### MAIN ###
def main():
  # Build rocket component
  head_rocket_component = HeadRocketComponent()
  return

  # Create simulation
  simulation = Simulation(head_rocket_component)

  # Start simulation
  simulation.start()



if __name__ == '__main__':
  main()
