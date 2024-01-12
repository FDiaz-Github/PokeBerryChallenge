import requests
import concurrent.futures
import os
from typing import List


def get_berry_data() -> List:
    '''
    This function collects berry stats from the collected urls, then concurrently fetches the berry details
    in order to speed up the process
    :return: List of berry stats for all berries given by the pokeapi berry endpoint
    '''
    pokeapi_url = os.getenv('POKEAPI_URL', "https://pokeapi.co/api/v2/berry/")
    berry_urls = _get_all_berry_urls(pokeapi_url)
    all_berries = []

    # Using ThreadPoolExecutor to fetch berry details concurrently instead of one by one
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(_fetch_berry, url): url for url in berry_urls}
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                berry = future.result()
                all_berries.append(berry)
            except Exception as exc:
                print(f'Error fetching berry data: {exc}')

    return all_berries


def _get_all_berry_urls(url: str, berry_urls=[]) -> List:
    '''
    Function to get all berries from the berry endpoint.
    :param url: String of the pokeberry endpoint
    :return: A list of all the urls of the berries in the pokeapi database
    '''
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        berry_urls.extend([berry['url'] for berry in data['results']])
        if data['next']:
            return _get_all_berry_urls(data['next'], berry_urls)
    else:
        raise Exception("Failed to fetch data from PokeAPI")
    return berry_urls


def _fetch_berry(berry_url: str):
    '''
    Simple function to get information from a berry url
    :param berry_url: url for a poke api Berry
    :return: Json response
    '''
    response = requests.get(berry_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data for berry at {berry_url}")
