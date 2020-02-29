import requests
import urllib3
from pathlib import Path
from download_image import download_image


def get_hubble_collection(collection_name, directory_for_save):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)
    response.raise_for_status()
    images_id = []
    for image_record in response.json():
        fetch_hubble_image(image_record['id'],
                           directory_for_save)


def fetch_hubble_image(image_id, directory_for_save):
    hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(hubble_url)
    response.raise_for_status()
    image_link = f"https:{response.json()['image_files'][-1]['file_url']}"
    image_extension = Path(image_link).suffix
    download_image(image_link,
                   directory_for_save,
                   f'hubble_image_{image_id}{image_extension}')

