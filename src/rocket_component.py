from abc import ABC

from atmosphere import Atmosphere
from position import Position



class RocketComponent(ABC):
  
  def __init__(self, position: Position) -> None:
    self.atmosphere = Atmosphere(self.altitude)
    self.pos = position



# Concrete Components
class HeadRocketComponent(RocketComponent):

  def __init__(self, altitude=0) -> None:
    super().__init__(altitude)



# Abstract Decorator
class RocketComponentDecorator(RocketComponent):
  
  def __init__(self, rocket_component, altitude=0) -> None:
    super().__init__(altitude)
    self.rocket_component = rocket_component


  def set_rocket_component(self, rocket_component: 'RocketComponent') -> None:
    """
    Set the rocket component

    :param RocketComponent rocket_component: The rocket component to be coupled with self
    """
    self.rocket_component = rocket_component

  
  def decouple_rocket_component(self) -> RocketComponent:
    """
    Represent the decoupling of two rocket components

    :return RocketComponent: The RocketComponent that this object decorates
    """
    # Save off RocketComponent to return
    rocket_component = self.rocket_component

    # Remove decorator from self.rocket_component
    self.rocket_component = None
    
    return rocket_component