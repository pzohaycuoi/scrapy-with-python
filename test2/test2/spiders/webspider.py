import scrapy

class yoSpidy(scrapy.Spider):
    name = "scrapWebsite"
    start_urls = [
        'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/1/ha-noi.html',
    ]

    def parse(self, response):
        for items in response.css("div.content-item"): 
            yield {
                'title': items.css("div.ct_title a::text").get(),
                'road-width': items.css("span.road-width::text").get(),
                'floors': items.css("span.floors::text").get(),
                'bedroom': items.css("span.bedroom::text").get(),
                'ct_dt': items.css("div.ct_dt label::text").get(),
            }
