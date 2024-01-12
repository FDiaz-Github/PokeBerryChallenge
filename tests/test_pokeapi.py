
import pytest
from unittest.mock import patch
from pokeapi import get_berry_data


@pytest.fixture
def mock_berry_urls():
    return [
        'https://pokeapi.co/api/v2/berry/1/',
        'https://pokeapi.co/api/v2/berry/2/',
    ]


@patch('pokeapi._get_all_berry_urls')
def test_get_berry_data(mock_get_all_berry_urls, mock_berry_urls):
    mock_get_all_berry_urls.return_value = mock_berry_urls
    berries = get_berry_data()
    assert len(berries) == len(mock_berry_urls)
    assert 'growth_time' in berries[0]
