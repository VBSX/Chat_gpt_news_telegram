from dotenv import load_dotenv
import os
import openai
from news_requets import GetAllNewsRss

class OpenGptChat():
    def __init__(self):
        load_dotenv()
        g1_link = 'https://g1.globo.com/rss/g1/'
        uol_link = 'http://rss.uol.com.br/feed/noticias.xml'
        bbc_link = 'https://feeds.bbci.co.uk/portuguese/rss.xml'
        self.g1_news = GetAllNewsRss(g1_link).get_only_title()
        self.uol_news = GetAllNewsRss(uol_link).get_only_title()
        self.bbc_news = GetAllNewsRss(bbc_link).get_only_title()
        self.all_news = self.g1_news + self.uol_news + self.bbc_news
        self.gpt_api_key = os.getenv('GPT_API_KEY')
        openai.api_key = self.gpt_api_key
        self.engine = 'text-davinci-003'
        self.prompt = f'com base nessa lista que estou te dando agora {self.all_news} \ncoloque em topicos as noticias mais importantes e as que mais impactaram o dia (coloque o link junto com a sua espectiva noticia)'
        ' filtre as informações, por exemplo textos falando sobre o o veiculo de midia(Como g1, ou tv gazeta, ou uol) foque'
        'somente na noticia'
        self.temperature = 0.5
        self.max_tokens = 2048
        self.top_p = 1
        print(self.all_news)
        
    def resumo(self):
        response = openai.Completion.create(
            engine =self.engine,
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=self.top_p)
        return response['choices'][0]['text']
    
if __name__ == '__main__':
    gpt = OpenGptChat()
    print(gpt.resumo())