import sys

# Order must conform to DAG (Directed Acyclic Graph)

import src.atmosphere as atmosphere
sys.modules['atmosphere'] = atmosphere

import src.position as position
sys.modules['position'] = position

import src.vector as vector
sys.modules['vector'] = vector

import src.coordinate_system as coordinate_system
sys.modules['coordinate_system'] = coordinate_system

import src.rocket_component as rocket_component
sys.modules['rocket_component'] = rocket_component

import src.simulation_data as simulation_data
sys.modules['simulation_data'] = simulation_data

import src.simulation as simulation
sys.modules['simulation'] = simulation