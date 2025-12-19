
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError
from test_project.utils.http_client import get_json


def test_get_json_success():
    # Patch 'request.get' where it is used
    with patch("test_project.utils.http_client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        result = get_json("https://fackurl.example")
        assert result == {"key": "value"}
        mock_get.assert_called_with("https://fackurl.example", timeout=5)



def test_get_json_http_error():
    # Patch 'requests.get' where it is used
    with patch("test_project.utils.http_client.requests.get") as mock_get:
        # Simulate a response that raises HTTPError
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = HTTPError("503 Server Error")
        mock_get.return_value = mock_response

        # Verify that our wrapper raises RuntimeError
        with pytest.raises(RuntimeError) as exc_info:
            get_json("https://fackurl.example")

        assert "Failed to fetch JSON" in str(exc_info.value)
        mock_get.assert_called_once_with("https://fackurl.example", timeout=5)