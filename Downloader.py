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
        for _ in range(self.count_of_img):
            file_name = self.generate_id(LENGTH)
            url = self.generate_link(file_name)
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content
            time.sleep(0.2)
            soup = BeautifulSoup(page), file_name
            image_url = soup.find('img', class_="no-click screenshot-image")['src']
            image_binary = requests.get(image_url, stream = True).content
            try:
                with open(f'{file_name}.jpg', "wb") as handler:
                    handler.write(image_binary)
            except:
                pass

def main():
    #Downloader = LightLoader(2)
    #Downloader.run()

if __name__ == '__main__':
    main()
