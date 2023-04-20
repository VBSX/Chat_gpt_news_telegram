import requests
from rss_parser import Parser
from dotenv import load_dotenv
import os
from time import sleep

class GetAllNewsRss():
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.api_key = os.getenv('CUTTLY_API_KEY')
        load_dotenv()
        
    def get_all_news(self):
        parser = Parser(xml=self.response.content, limit=5)
        feed = parser.parse()
        
        return feed.feed
    
    def get_only_title(self):
        parser = Parser(xml=self.response.content, limit=1)
        feed = parser.parse()
        return [f'{item.title} / link: {self.link_shortener(item.link)}' for item in feed.feed]

    def link_shortener(self, url):
        api_url = f"https://cutt.ly/api/api.php?key={self.api_key}&short={url}"
        response = requests.get(api_url)
        # sleep(20)
        try:
            data = response.json()
            data_url = data["url"]
            shortened_url = data_url["shortLink"]
            return  shortened_url
        except requests.exceptions.JSONDecodeError as er:
            print(er)
if __name__ == '__main__':
    rss_g1 = 'https://g1.globo.com/rss/g1/'
    news_g1 = GetAllNewsRss(rss_g1)
    # for item in news_g1.get_all_news():
    #     print(item.title,'\n')
    #     print(item.description,'\n') 
    print(news_g1.get_only_title())