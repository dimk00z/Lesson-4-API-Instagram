import requests
import urllib3
from pathlib import Path
from download_image import download_image


def fetch_spacex_last_launch(directory_for_save):
    spacex_lastest_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(spacex_lastest_url)
    response.raise_for_status()
    last_launch_image_links = response.json()['links']['flickr_images']
    for image_number, image_url in enumerate(last_launch_image_links):
        download_image(image_url,
                       directory_for_save,
                       f'spacex{image_number+1}.jpg')
