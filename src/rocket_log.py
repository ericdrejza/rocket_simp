import pandas as pd

class RocketLog:
  def __init__(self) -> None:

    self.data = pd.DataFrame(columns=[
      'time', # time
      'rocket_component_id', # Unique rocket component identifier
      'x', # x position
      'y', # y position
      'v_magnitude', # magnitude of velocity
      'v_alpha', # angle of velocity
      'v_direction', # direction of velocity
      'v_x', # x value of velocity
      'v_y', # y value of velocity
      'fuel_mass', # mass of fuel
      'structure_mass', # mass of structure
      'drag_force',
      'gravity_force',
      'lift_force',
      'thrust_force',
      'atmosphere_density',
      'atmosphere_gravity',
      'atmosphere_pressure',
      'atmosphere_temperature',
      'atmosphere_viscosity'
    ])