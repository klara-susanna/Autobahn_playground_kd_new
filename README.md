# Autobahn Playground

Welcome to the Autobahn Playground! This project simulates a car's speed management on the famous German Autobahn.

## Features

- **Random Speed Generation**: Each car starts with a random speed between 105.0 and 135.0 km/h.
- **Speed Update Based on Traffic Information**: The car's speed can be updated based on provided traffic information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/autobahn_playground.git
    ```
2. Navigate to the project directory:
    ```sh
    cd autobahn_playground
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the `Car` class, you can create an instance and call its methods:

```python
from src.autobahn.vehicle import Car

# Create a car instance
my_car = Car()

# Get the current speed
print(f"Current speed: {my_car.get_speed()} km/h")

# Update the speed based on traffic information
traffic_info = {"averageSpeed": 90.0}
my_car.update_speed(traffic_info)
print(f"Updated speed: {my_car.get_speed()} km/h")
