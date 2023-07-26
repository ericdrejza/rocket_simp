import sys

# Order must conform to DAG (Directed Acyclic Graph)

import src.atmosphere as atmosphere
sys.modules['atmosphere'] = atmosphere

import src.position as position
sys.modules['position'] = position

import src.vector as vector
sys.modules['vector'] = vector

import src.rocket_log as rocket_log
sys.modules['rocket_log'] = rocket_log

import src.rocket_component as rocket_component
sys.modules['rocket_component'] = rocket_component

import src.simulation as simulation
sys.modules['simulation'] = simulation