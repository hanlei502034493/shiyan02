# -*- coding: utf-8 -*-
import scrapy
from ..items import HahaItem

class KaoSpider(scrapy.Spider):
    name = 'kao'
    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.21food.cn/']

    def parse(self, response):
        with open('./htmls/yuan.html',"w",encoding="utf-8")as f:
            f.write(response.text)
        yield scrapy.Request(url="https://www.21food.cn/product/search_keys-%BA%A3%CF%CA.html",callback=self.xiang_parse)
    def xiang_parse(self,response):
        with open('./htmls/hai.html','w',encoding='utf-8')as f:
            f.write(response.text)
        dd_list=response.xpath('//dd/table[@class="st_le_lef"]/tr/td/a')
        for dd in dd_list:
            link="https://www.21food.cn"+dd.xpath('./@href').extract_first()
            title=dd.xpath('./@title').extract_first()
            yield scrapy.Request(url=link,callback=self.hai_parse,meta={"title":title,"link":link})
    def hai_parse(self,response):
        title=response.meta["title"]
        link=response.url
        riqi=response.xpath('//tr/td[@align="right"]/span/text()').extract_first()
        name="海鲜"
        yield HahaItem(name=name,title=title,link=link,riqi=riqi)