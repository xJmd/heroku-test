import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.geturl = requests.get(self.url)
        self.soup = BeautifulSoup(self.geturl.text, 'html.parser')

    def get_data(self):
        title = self.soup.find("meta", property="og:title")['content']
        thumbnail_url = self.soup.find("meta", property="og:image")['content']
        upload_date = self.soup.find("meta", itemprop="uploadDate")['content']
        return title, thumbnail_url, upload_date