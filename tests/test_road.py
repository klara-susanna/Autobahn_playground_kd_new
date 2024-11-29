import pytest
import pandas as pd
import folium
from autobahn.road import (
    get_warnings,
    TrafficWarning,
    calculate_traffic_length,
    map_plot,
)


@pytest.fixture
def mock_warnings():
    return [
        {
            "isBlocked": True,
            "display_type": "type",
            "subtitle": "subtitle",
            "title": "title",
            "startTimestamp": "timestamp",
            "delayTimeValue": 10,
            "abnormalTrafficType": "type",
            "averageSpeed": 60.0,
            "description": "description",
            "routeRecommendation": "route",
            "lorryParkingFeatureIcons": [],
            "geometry": {"coordinates": [[8.682127, 50.110924]]},
        }
    ]


@pytest.fixture
def mock_coordinates():
    return pd.DataFrame({"lat": [50.110924, 50.111924], "long": [8.682127, 8.683127]})


@pytest.fixture
def mock_df():
    return pd.DataFrame(
        {
            "lat": [50.110924, 50.111924],
            "long": [8.682127, 8.683127],
            "aveg_speed": [60, 50],
        }
    )


@pytest.fixture
def mock_response(monkeypatch, mock_warnings):
    class MockResponse:
        def json(self):
            return {"warning": mock_warnings}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)


def test_get_warnings(mock_response):
    warnings = get_warnings("A1")
    assert isinstance(warnings, list)
    assert len(warnings) > 0


def test_traffic_warning(mock_warnings):
    data = mock_warnings[0]
    warning = TrafficWarning(data)
    assert warning.isBlocked
    assert warning.display_type == "type"
    assert warning.subtitle == "subtitle"
    assert warning.title == "title"
    assert warning.startTimestamp == "timestamp"
    assert warning.delayTimeValue == 10
    assert warning.abnormalTrafficType == "type"
    assert warning.averageSpeed == 60.0
    assert warning.description == "description"
    assert warning.routeRecommendation == "route"
    assert warning.lorryParkingFeatureIcons == []
    assert isinstance(warning.geo_df, pd.DataFrame)


def test_calculate_traffic_length(mock_coordinates):
    length = calculate_traffic_length(mock_coordinates)
    assert length > 0


def test_calculate_traffic_length_with_NaN():
    coordinates = pd.DataFrame({"lat": [10.0, 12.0, None], "long": [0.0, 0.0, 0.0]})
    expected_length = 222.0
    actual_length = calculate_traffic_length(coordinates)
    assert abs(expected_length - actual_length) < 1.0


def test_map_plot(mock_df):
    m = map_plot([mock_df])
    assert isinstance(m, folium.Map)
