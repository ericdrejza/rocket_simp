import pandas as pd

class RocketLog:
  def __init__(self) -> None:

    self.data = pd.DataFrame(columns=[
      'rocket_component_id', # Unique rocket component identifier
      'time', # time
      'pos_x', # x position
      'pos_y', # y position
      'pos_z', # z position
      'velocity_magnitude', # magnitude of velocity
      'velocity_alpha', # angle of velocity
      'velocity_direction', # direction of velocity
      'velocity_x', # x value of velocity
      'velocity_y', # y value of velocity
      'velocity_z',
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

  
  def add(self, rocket_component, time):
    """
    Add a RocketComponent data to the DataFrame

    :param rocket_component: _description_
    :type rocket_component: _type_
    :param time: _description_
    :type time: _type_
    """
    data = pd.DataFrame({
      'id': rocket_component.id,
      'time': time,
      'pos_x': rocket_component.position.x,
      'pos_y': rocket_component.position.y,
      'pos_z': rocket_component.position.z,
      'velocity': rocket_component.velocity,
      'velocity_magnitude': rocket_component.velocity_magnitude,
      'velocity_alpha': rocket_component.velocity_alpha,
      'velocity_direction': rocket_component.velocity_direction,
      'velocity_x': rocket_component.velocity_x,
      'velocity_y': rocket_component.velocity_y,
      'velocity_z': rocket_component.velocity_z,
      'mass_fuel': rocket_component.mass_fuel,
      'mass_structure': rocket_component.mass_structure,
      'force_drag': rocket_component.force_drag,
      'force_gravity': rocket_component.force_gravity,
      'force_lift': rocket_component.force_lift,
      'force_thrust': rocket_component.force_thrust,
      'atm_density': rocket_component.atm_density,
      'atm_gravity': rocket_component.atm_gravity,
      'atm_pressure': rocket_component.atm_pressure,
      'atm_temperature': rocket_component.atm_temperature,
      'atm_viscosity': rocket_component.atm_viscosity
    })
    self.data.add(data)
    return data