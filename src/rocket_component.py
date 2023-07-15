from abc import ABC

from atmosphere import Atmosphere


class RocketComponent(ABC):
  
  def __init__(self, altitude=0) -> None:
    self.altitude = altitude
    self.atmosphere = Atmosphere(self.altitude)



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
    self.rocket_component = rocket_component