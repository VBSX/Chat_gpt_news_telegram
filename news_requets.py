import requests
from rss_parser import Parser
from dotenv import load_dotenv
import os

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
        parser = Parser(xml=self.response.content, limit=5)
        feed = parser.parse()
        return [f'{item.title} / link: {self.link_shortener(item.link)}' for item in feed.feed]

    def link_shortener(self, url):
        # Aqui é utilizado a API do encurtador.dev, onde podemos encurtar os links de 
        # maneira gratuita e muito rapida
        headers = {
            'content-type': 'application/json',
        }
        json_data = {
            'url': url,
        }
        response = requests.post('https://api.encurtador.dev/encurtamentos', headers=headers, json=json_data)
        try:
            data = response.json()
            return data['urlEncurtada']   
        except requests.exceptions.JSONDecodeError as er:
            print(er)
if __name__ == '__main__':
    rss_g1 = 'https://g1.globo.com/rss/g1/'
    news_g1 = GetAllNewsRss(rss_g1)
    # for item in news_g1.get_all_news():
    #     print(item.title,'\n')
    #     print(item.description,'\n') 
    print(news_g1.get_only_title())