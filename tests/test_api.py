from unittest.mock import patch
from api import get_nutrition_data
import pytest

@patch("api.requests.get")
def test_get_nutrition_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "foods": [{"description": "Burger"}]
    }
    result = get_nutrition_data("burger")

    assert result is not None

@patch("api.requests.get")
def test_get_empty_nutrition_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "foods": []
    }
    result = get_nutrition_data("nothing")

    assert result is None

@patch("api.requests.get")
def test_get_raises_code_nutrition_data(mock_get):
    mock_get.return_value.status_code = 500

    with pytest.raises(Exception):
        raise Exception
