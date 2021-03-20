from bs4 import BeautifulSoup
import requests
import time, random, os, string

LENGTH = 6
class LightLoader:
    def __init__(self, count_of_img = 10, save_path = None):
        self.count_of_img = count_of_img
        self.save_path = save_path

    def generate_id(self, size):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

    def generate_link(self, file_name):
        return "https://prnt.sc/" + file_name

    def run(self):
        file_name = self.generate_id(LENGTH)
        url = self.generate_link(file_name)
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
        soup = BeautifulSoup(page)
        print(soup.prettify())



Downloader = LightLoader(10)
Downloader.run()
