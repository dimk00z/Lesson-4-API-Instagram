import glob
import os
import time
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_hubble_collection
from pathlib import Path
from PIL import Image
from resizeimage import resizeimage
from dotenv import load_dotenv
from instabot import Bot


def make_image_square(image_file_name):
    image = Image.open(image_file_name)
    x, y = image.size
    size = min(x, y, 1080)
    image = resizeimage.resize_crop(image, [size, size])
    image.save(image_file_name, image.format)


def get_images_list():
    image_path = f"{str(Path().absolute())}\images"
    image_files = [f for f in glob.glob(f"{image_path}\*", recursive=False)]
    return image_files


def get_login_pass():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    return os.getenv("LOGIN"), os.getenv("PASSWORD")


def post_image_to_instagram(user, password, image_file_path):
    bot = Bot()
    bot.login(username=user, password=password)
    try:
        bot.upload_photo(image_file_path)
    except Exception as e:
        bot.logger.error("\033[41mERROR...\033[0m")
        bot.logger.error(str(e))


def main():
    directory_for_save = 'images'
    fetch_spacex_last_launch(directory_for_save)
    get_hubble_collection('wallpaper', directory_for_save)
    instagram_login, instagram_password = get_login_pass()
    for image_file_name in get_images_list():
        make_image_square(image_file_name)
        post_image_to_instagram(instagram_login,
                                instagram_password,
                                image_file_name)
        time.sleep(3)


if __name__ == '__main__':
    main()
