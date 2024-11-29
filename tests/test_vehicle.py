import pytest
from autobahn.vehicle import Car
from test_road import mock_warnings as road_mock_warnings


@pytest.fixture
def car():
    return Car()


def test_car_default_speed(car):
    speed = car.get_speed()
    assert 105 <= speed <= 135


def test_car_speed_in_traffic_zone(car, road_mock_warnings):
    traffic_info = road_mock_warnings[0]
    car.update_speed(traffic_info)
    assert car.get_speed() == 60.0


def test_car_speed_in_traffic_zone_no_average_speed(car, road_mock_warnings):
    traffic_info = road_mock_warnings[0]
    traffic_info["averageSpeed"] = None
    car.update_speed(traffic_info)
    assert car.get_speed() == 80
