import scrapy


class PinyicheSpider(scrapy.Spider):
    name = "pinyiche"
    allowed_domains = ["prod.pinyiche.club"]
    start_urls = ["http://prod.pinyiche.club/"]

    def parse(self, response):
        print(response.body)
        pass
