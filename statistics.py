from typing import List, Dict, Any
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np



def calculate_stats(berry_stats: List) -> Dict[str, Any]:
    '''
    Function that calculates berry statistics based on a collection of berry stats.
    :param berry_stats: Collection of berry stats
    :return: Dictionary with specific stats regarding growth time and collection of the berry names analyzed
    '''
    data = [(berry['item']['name'], berry['growth_time']) for berry in berry_stats]
    berry_names, growth_times = zip(*data)
    min_growth_time = min(growth_times)
    median_growth_time = float(np.median(growth_times))
    max_growth_time = max(growth_times)
    variance_growth_time = float(np.var(growth_times, ddof=1))
    mean_growth_time = float(np.mean(growth_times))
    # Since itemfreq from scipy is deprecated, using np.unique
    frequencies = np.unique(growth_times, return_counts=True)
    frequency_growth_time = {int(time): int(count) for time, count in zip(*frequencies)}
    stats = {
        'berries_names': berry_names,
        'min_growth_time': min_growth_time,
        'median_growth_time': median_growth_time,
        'max_growth_time': max_growth_time,
        'variance_growth_time': variance_growth_time,
        'mean_growth_time': mean_growth_time,
        'frequency_growth_time': frequency_growth_time
    }
    return stats


def create_histogram(frequency_growth_time, filename='histogram.png'):
    '''
    Generates a histogram based on the stats frequency_growth_time.
    :param frequency_growth_time:
    :param filename:
    :return: Histogram generated
    '''
    growth_times = list(frequency_growth_time.keys())
    frequencies = list(frequency_growth_time.values())

    plt.bar(growth_times, frequencies, color='blue', alpha=0.7)
    plt.title('Frequency of Berry Growth Times')
    plt.xlabel('Growth Time')
    plt.ylabel('Frequency')

    plt.savefig(filename)
    plt.close()