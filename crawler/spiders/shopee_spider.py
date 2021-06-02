import scrapy
import urllib

class ShopeeSpider(scrapy.Spider):
    name = 'shopee'
    custom_settings = {
        'FEEDS': {
            'shopee.jl': {
                'format': 'jsonlines',
                'encoding': 'utf8',
                'overwrite': True,
            },
        },
    }

    def start_requests(self):
        keyword = '手機保護殼'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
            'x-api-source': 'pc',
            'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'
        }
        url = 'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'
        yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        pass



