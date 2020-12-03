import scrapy

class webscrapper (scrapy.Spider):
    name = "webURL"
    start_urls = [
        'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/1/ha-noi.html'
    ]

    def parse(self, response):
        for items in response.xpath('//*[@class="content-item"]'):
            yield {
                'title': items.xpath('//*[@class="ct_title"]/text()').get()
            }