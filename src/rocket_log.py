import importlib
import pandas as pd
import sys
import rocket_component as rc

class RocketLog:
  def __init__(self) -> None:

    self.data = pd.DataFrame(columns=[
      'id', # Unique rocket component identifier
      'time', # time
      'pos_x', # x position
      'pos_y', # y position
      'pos_z', # z position
      'velocity_x', # x value of velocity
      'velocity_y', # y value of velocity
      'velocity_z',
      'velocity_r', # magnitude of velocity
      'velocity_theta', # angle of velocity
      'mass_fuel', # mass of fuel
      'mass_structure', # mass of structure
      'drag_force_x',
      'drag_force_y',
      'drag_force_r',
      'drag_force_theta',
      'gravity_force_x',
      'gravity_force_y',
      'gravity_force_r',
      'gravity_force_theta',
      'lift_force_x',
      'lift_force_y',
      'lift_force_r',
      'lift_force_theta',
      'thrust_force_x',
      'thrust_force_y',
      'thrust_force_r',
      'thrust_force_theta',
      'atm_density',
      'atm_gravity',
      'atm_pressure',
      'atm_temperature',
      'atm_viscosity'
    ])


  def add(self, rocket_component: 'rc.RocketComponent', time):
    """
    Add a RocketComponent data to the DataFrame

    :param rocket_component: _description_
    :type rocket_component: _type_
    :param time: _description_
    :type time: _type_
    """
    data = pd.DataFrame([{
      'id': rocket_component.id,
      'time': time,
      'pos_x': rocket_component.position.x,
      'pos_y': rocket_component.position.y,
      'pos_z': 0,
      'velocity_x': rocket_component.velocity.x,
      'velocity_y': rocket_component.velocity.y,
      'velocity_z': 0,
      'velocity_r': rocket_component.velocity.r,
      'velocity_theta': rocket_component.velocity.theta,
      'mass_fuel': rocket_component.mass_fuel,
      'mass_structure': rocket_component.mass_structure,
      'drag_force_x': rocket_component.drag_force.x,
      'drag_force_y': rocket_component.drag_force.y,
      'drag_force_r': rocket_component.drag_force.r,
      'drag_force_theta': rocket_component.drag_force.theta,
      'gravity_force_x': rocket_component.gravity_force.x,
      'gravity_force_y': rocket_component.gravity_force.y,
      'gravity_force_r': rocket_component.gravity_force.r,
      'gravity_force_theta': rocket_component.gravity_force.theta,
      'lift_force_x': rocket_component.lift_force.x,
      'lift_force_y': rocket_component.lift_force.y,
      'lift_force_r': rocket_component.lift_force.r,
      'lift_force_theta': rocket_component.lift_force.theta,
      'thrust_force_x': rocket_component.thrust_force.x,
      'thrust_force_y': rocket_component.thrust_force.y,
      'thrust_force_r': rocket_component.thrust_force.r,
      'thrust_force_theta': rocket_component.thrust_force.theta,
      'atm_density': rocket_component.atmosphere.density,
      'atm_gravity': rocket_component.atmosphere.gravity,
      'atm_pressure': rocket_component.atmosphere.pressure,
      'atm_temperature': rocket_component.atmosphere.temperature,
      'atm_viscosity': rocket_component.atmosphere.viscosity
    }])
    self.data = pd.concat([self.data, data.round(3)], ignore_index=True)
    return data