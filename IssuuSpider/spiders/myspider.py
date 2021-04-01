import scrapy
import json
from IssuuSpider.items import IssuuspiderItem


class MySpider(scrapy.Spider):
    # MySpider Name
    name = "alex"
    website = "https://issuu.com"
    state_code = "Kb37l2wNAVkOEEW_70FHjzjTWVJRjCUuoK59Lac8mt7okzZkJPl5yqH--U4Cdtc4kSWMoLND1SGzqxkl6X1zi9mNZ97Fv_ux8dPmG0LS1zBkGlc6fGXSY35_vX9rnl7ojoImVlwsiwFeQAliKzlcUQfbLoqQN6MyUWgvB7FIY8SEROh3izzvPze3DB2uJQ== "
    start_urls = [
        'https://issuu.com/call/stream/api/publicationsearch/1/0/cont/master-70?state={}&pageSize=20&format=json'.format(
            state_code)
    ]

    # def detail_parse(self, response):
    #     with open('myweb.html', 'wb') as f:
    #         f.write(response.body)

    def meta_parse(self, response, detail_url):
        json_like_data = json.loads(response.text)
        item = IssuuspiderItem()
        item['follow'] = int(json_like_data["following"]["count"])
        item['like'] = int(json_like_data["like"]["count"])
        item['detail_url'] = detail_url
        yield item

    def parse(self, response):
        json_data = json.loads(response.text)
        detail_urls = []
        like_urls = []
        for item in json_data["rsp"]["_content"]['stream']:
            ownerUsername = item['content']['ownerUsername']
            publicationName = item['content']['publicationName']
            # 详情页
            detail_url = self.website + r"/" + ownerUsername + r"/docs/" + publicationName
            detail_urls.append(detail_url)
            like_url = r"https://issuu.com/call/document-page/" + ownerUsername + r"/" + publicationName + r"/meta-data"
            like_urls.append(like_url)
        for like_url, detail_url in zip(like_urls, detail_urls):
            yield scrapy.Request(url=like_url,
                                 callback=self.meta_parse,
                                 cb_kwargs=dict(detail_url=detail_url))
        if json_data["rsp"]["_content"]["continuation"] is not None:
            next_website = self.website + json_data["rsp"]["_content"]["continuation"] + "&pageSize=20&format=json"
            yield response.follow(next_website, self.parse)
