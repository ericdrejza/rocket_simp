# rocket_simp
# Rocket Simulator Program

The Rocket Simulator Program is designed to simulate the flight of a rocket
given parameters of the environment, rocket, and potentially others.


<hr />

## Requirements / Dependencies

<strong>requirements.txt</strong> will track the required packages for the project.

To install the required packages for this project, from the repo root, run:
  - `$ pip3 install -r requirements.txt`
    - Be sure to do this while in your virtual environment

To update requirements.txt, from the repo root, run:
  - `$ pip3 freeze > requirements.txt`
    - Be sure to do this while in your virtual environment and have all packages installed that you want update the requirements.txt with

<hr />

## Unit Tests
Tests are kept in the tests/ directory.

Before running any unittest command cd into the repo root.
  - `$ cd .../rocket_simp`

Tests can be run individually using:
  - `$ python3 -m unittest <test path>`

All tests can be run using:
  - `$ python3 -m unittest`
  - `$ python3 -m unittest discover <tests directory path>`
