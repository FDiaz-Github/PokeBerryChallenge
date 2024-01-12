import pytest
from statistics import calculate_stats
import numpy as np


@pytest.fixture
def berry_data():
    return [
        {'item': {'name': 'cheri'}, 'growth_time': 5},
        {'item': {'name': 'chesto'}, 'growth_time': 10}
    ]


def test_calculate_stats(berry_data):
    stats = calculate_stats(berry_data)
    growth_times = [5,10]
    berry_names = ('cheri', 'chesto')
    assert stats['berries_names'] == berry_names
    assert stats['min_growth_time'] == min(growth_times)
    assert stats['median_growth_time'] == float(np.median(growth_times))
    assert stats['max_growth_time'] == max(growth_times)
    assert stats['variance_growth_time'] == float(np.var(growth_times, ddof=1))
    assert stats['mean_growth_time'] == float(np.mean(growth_times))
    frequencies = np.unique(growth_times, return_counts=True)
    expected_frequency = {int(time): int(count) for time, count in zip(*frequencies)}
    assert stats['frequency_growth_time'] == expected_frequency
