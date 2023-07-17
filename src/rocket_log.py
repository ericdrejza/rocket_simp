import pandas as pd

class RocketLog:
  def __init__(self) -> None:

    self.data = pd.DataFrame(columns=[
      'time', # time
      'rocket_component_id', # Unique rocket component identifier
      'pos_x', # x position
      'pos_y', # y position
      'velocity_magnitude', # magnitude of velocity
      'velocity_alpha', # angle of velocity
      'velocity_direction', # direction of velocity
      'velocity_x', # x value of velocity
      'velocity_y', # y value of velocity
      'mass_fuel', # mass of fuel
      'mass_structure', # mass of structure
      'force_drag',
      'force_gravity',
      'force_lift',
      'force_thrust',
      'atm_density',
      'atm_gravity',
      'atm_pressure',
      'atm_temperature',
      'atm_viscosity'
    ])