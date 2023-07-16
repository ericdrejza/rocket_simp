import pandas as pd

class RocketLog:
  def __init__(self) -> None:

    self.data = pd.DataFrame(columns=[
      'time',
      'rocket_component_id',
      'x',
      'y',
      'v',
      'alpha',
      'direction',
      'v_x',
      'v_y',
      'fuel_mass'
    ])