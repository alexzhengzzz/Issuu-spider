import scrapy
import json
from IssuuSpider.items import IssuuspiderItem


class MySpider(scrapy.Spider):
    name = "alex"
    website = "https://issuu.com"
    state_code = "nBJyxXnRXwn2qJz7in9xh_a6dwKjLxLR6heWBJUy5VyXYa_qVvYRfqdF3YPTPudVMaZITEjB0vDcFf46-M6OIsuxv8pwZgxpyMiPihHMfq7HDTnE_zTkZnE-CoxeyZAp4929WdXK6P8aSfay4RzLngBJ8gpxGD1fDdIdrH2SD3wSTz6ytw=="


    def start_requests(self):
        urls = [
            'https://issuu.com/call/stream/api/publicationsearch/1/0/cont/master-45?state={}&pageSize=20&format=json'.format(self.state_code)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def detail_parse(self, response):
        with open('myweb.html', 'wb') as f:
            f.write(response.body)

    def meta_parse(self, response, detail_url):
        json_like_data = json.loads(response.text)
        item = IssuuspiderItem()
        item['follow'] = int(json_like_data["following"]["count"])
        item['like'] = int(json_like_data["like"]["count"])
        item['detail_url'] = detail_url
        yield item


    def parse(self, response):
        json_data = json.loads(response.text)
        ajax_next_website = self.website + json_data["rsp"]["_content"]["continuation"] + "&pageSize=20&format=json"
        print(ajax_next_website)
        detail_urls = []
        like_urls = []
        for item in json_data["rsp"]["_content"]['stream']:
            ownerUsername = item['content']['ownerUsername']
            publicationName = item['content']['publicationName']
            # 详情页
            detail_url = self.website + r"/" + ownerUsername + r"/docs/"+ publicationName
            detail_urls.append(detail_url)
            like_url = r"https://issuu.com/call/document-page/" + ownerUsername + r"/" + publicationName + r"/meta-data"
            like_urls.append(like_url)
        for like_url, detail_url in zip(like_urls, detail_urls):
            yield scrapy.Request(url=like_url,
                                 callback=self.meta_parse,
                                 cb_kwargs=dict(detail_url=detail_url))
        yield scrapy.Request(url=ajax_next_website,
                                     callback=self.parse)

