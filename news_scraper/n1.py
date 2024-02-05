"""import scrapy
import json

class NewsTitleSpider(scrapy.Spider):
    name = 'NewsTitleSpider'
    start_urls = ['https://www.isual.it/distribuzione-aggiornamenti-aziendali/']

    def parse(self, response):
        # Estrarre i titoli (elementi <h1>)
        news_titles = response.css('h1::text').extract()

        # Estrarre il contenuto dell'articolo
        article_content = response.css('div.entry-content p::text').extract()

        # Salva i titoli in un file JSON
        with open('news_titles.json', 'w', encoding='utf-8') as json_file:
            json.dump(news_titles, json_file, ensure_ascii=False, indent=2)

        # Salva i titoli in un file CSV
        with open('news_titles.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_file.write('Titolo,Contenuto\n')
            for title, content in zip(news_titles, article_content):
                csv_file.write(f'"{title}","{content}"\n')

        # Stampa i titoli estratti
        for title in news_titles:
            self.log(title)"""

