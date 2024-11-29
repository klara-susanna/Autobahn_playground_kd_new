import random


class Car:
    """
    A class to represent a car with speed management.
    """

    def __init__(self):
        """
        Initialize the car with a default speed.
        """
        self.speed = self._default_speed()

    def _default_speed(self):
        """
        Generate a default speed for the car.

        Returns:
            float: A random speed between 105.0 and 135.0.
        """
        return random.uniform(105.0, 135.0)

    def get_speed(self):
        """
        Get the current speed of the car.

        Returns:
            float: The current speed of the car.
        """
        return self.speed

    def update_speed(self, traffic_info):
        """
        Update the speed of the car based on traffic information.

        Args:
            traffic_info (dict): A dictionary containing traffic information.
        """
        if traffic_info.get("averageSpeed") is not None:
            self.speed = traffic_info["averageSpeed"]
        else:
            self.speed = 80
