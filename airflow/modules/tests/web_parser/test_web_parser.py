from unittest.mock import patch
import pytest
from pytest import fixture

from ..fixtures import web_parser, response  


@patch("parser.web_parser.get")
def test_get_content(mock_get, web_parser):
    expected = "TEST CONTENT"
    
    mock_get.return_value.content = "TEST CONTENT" 
    mock_get.return_value.status_code = 200
    mock_get.return_value.headers['Content-Type'] = "text/html"

    result = web_parser.get_content()

    assert result == expected


@pytest.mark.parametrize(
    "status_code, expected",
    [(200, True), (403, False), (500, False)]
)
def test_is_good_response(web_parser, response, status_code, expected):
    http_response = response(status_code)

    result = web_parser.is_good_response(http_response)
    
    assert result == expected
