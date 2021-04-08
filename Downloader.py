import time
import random
import os
import string
import requests
from bs4 import BeautifulSoup


DIRNAME = "Downloaded"
LENGTH = 6


class LightLoader:
    def __init__(self, count_of_img=5, save_path=os.getcwd()):
        self.count_of_img = count_of_img
        if not os.path.exists(DIRNAME):
            os.mkdir(DIRNAME)
        self.save_path = os.path.join(save_path, DIRNAME)

    @staticmethod
    def generate_id(size):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

    @staticmethod
    def generate_link(file_name):
        return "https://prnt.sc/" + file_name

    def run(self):
        current_count_of_img = 0
        while current_count_of_img < self.count_of_img:
            file_name = self.generate_id(LENGTH)
            url = self.generate_link(file_name)
            try:
                page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content
                time.sleep(0.1)
                soup = BeautifulSoup(page, features="html.parser")
                image_url = soup.find('img', class_="no-click screenshot-image")['src']
                image_binary = requests.get(image_url, stream=True).content
                path = os.path.join(self.save_path, file_name)
                with open(f'{path}.jpg', "wb") as handler:
                    handler.write(image_binary)
                current_count_of_img += 1
            except:
                pass


def main():
    downloader = LightLoader()
    downloader.run()


if __name__ == '__main__':
    main()
