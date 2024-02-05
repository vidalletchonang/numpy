"""import scrapy

class NewsTitleSpider(scrapy.Spider):
    name = "NewsTitleSpider"
    allowed_domains = ["isual.it"]
    start_urls = ["https://www.isual.it/distribuzione-aggiornamenti-aziendali/"]

    def parse(self, response):
        # Extraire les titres des actualités en utilisant un sélecteur CSS
        news_titles = response.css('h2.entry-title a::text').extract()

        # Imprimer les titres des actualités
        for title in news_titles:
            self.log(title)
# news_titles = response.css('h2.entry-title a::text').extract()"""

import csv
class NewsTitleSpider(scrapy.Spider):
    # ... (resto del codice)
    def parse(self, response):
        # Extraire les titres des actualités en utilisant un sélecteur CSS
        news_titles = response.css('h2.entry-title a::text').extract()

        # Imprimer les titres des actualités
        for title in news_titles:
            self.log(title)

        # Scrivere i titoli nel file CSV
        self.write_to_csv(news_titles)

    def write_to_csv(self, data):
        with open('news_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Scrivere l'intestazione
            writer.writeheader()

            # Scrivere i dati
            for title in data:
                writer.writerow({'Title': title})
