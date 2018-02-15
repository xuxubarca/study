# #引入文件
# import scrapy

# class MySpider(scrapy.Spider):
#     #用于区别Spider
#     name = "MySpider"
#     #允许访问的域
#     allowed_domains = []
#     #爬取的地址
#     start_urls = []
#     #爬取方法
#     def parse(self, response):
#         pass

import scrapy
import json
# import pymongo

#引入容器
from LhSpider.CourseItems import CourseItem

class LhSpider(scrapy.Spider):
    # #设置name
    # name = "LhSpider"
    # #设定域名
    # allowed_domains = ["imooc.com"]
    # #填写爬取地址
    # start_urls = ["http://www.imooc.com/course/list"]
    # #编写爬取方法
    # def parse(self, response):
    #     #实例一个容器保存爬取的信息
    #     item = CourseItem()
    #     #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
    #     #先获取每个课程的div
    #     for box in response.xpath('//div[@class="moco-course-list"]/a[@target="_self"]'):
    #         #获取每个div中的课程路径
    #         item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
    #         #获取div中的课程标题
    #         item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
    #         #获取div中的标题图片地址
    #         item['image_url'] = box.xpath('.//@src').extract()[0]
    #         #获取div中的学生人数
    #         item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
    #         #获取div中的课程简介
    #         item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
    #         #返回信息
    #         yield item

    # #设置name
    # name = "MySpider"
    # #设定域名
    # allowed_domains = ["qingdaodujia.cn"]
    # #填写爬取地址
    # start_urls = ["http://www.qingdaodujia.cn/"]


    name = "LhSpider"
    # avList = []
    def start_requests(self):
        # urls = [
        #     'http://www.luohua03.com/xxfj/ym/'
        # ]
        u = 'http://www.luohua03.com/xxfj/ym/index'
        r = '.html'
        urls = [u+str(x)+r for x in range(163,764)]
        for url in urls:
            if 'index0' in url:
                continue
            elif 'index1' in url:
                url.replace('index1','index')

            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # item = CourseItem()
        uList = []
        for sel in response.xpath('//li[@class="box-shadow"]'):
            # print(sel.extract())
            # print(sel.xpath('span/a/@href').extract()[0])
            u = 'http://www.luohua03.com' + sel.xpath('span/a/@href').extract()[0]
            # item['image_url'] = sel.xpath('a/img/@src').extract()[0]
            # print(sel.xpath('div[@class="xr"]/dt/a/text()').extract()[0])
            # print(sel.xpath('a/img/@src').extract()[0])
            # print(sel.xpath('div[@class="product-description"]/h1/a/text()').extract()[0])
            # print(sel.xpath('div[@class="product-description"]/div[@class="product-price-and-shipping"]/span[@class="price"]/text()').extract()[0])
            # print('-----------------------')
            
            uList.append(u)

            # item['link'] = sel.xpath('a/@href').extract()[0]
            # item['image_url'] = sel.xpath('a/img/@src').extract()[0]
            # item['name'] = sel.xpath('div[@class="product-description"]/h1/a/text()').extract()[0]
            # item['price'] = sel.xpath('div[@class="product-description"]/div[@class="product-price-and-shipping"]/span[@class="price"]/text()').extract()[0]
            # u = sel.xpath('a/@href').extract()[0]
            # yield scrapy.Request(url=u, meta={'item': item},callback=self.page)
        for url in uList:
            yield scrapy.Request(url=url,callback=self.page)
        # print(json.dumps(uList))
            

    def page(self, response):
        item = CourseItem()
        # print(response.body)
        # item = response.meta['item']
        # for sel in response.xpath('//div[@class="lemma-summary"]'):
        #     item['info'] = sel.xpath('div/text()').extract()[0]
        #     yield item
        # for sel in response.xpath('//div[@class="info"]/ul'):
            # print(sel.extract())
            # print(sel.xpath('li[3]/h6[1]/text()').extract()[0])#aid
            # print(sel.xpath('li[1]/a/text()').extract()[0]) 
            # av = sel.xpath('h6[1]/text()').extract()[0]
            # item['id'] = sel.xpath('h6[1]/text()').extract()[0]
            # self.avList.append(av)
        # print(json.dumps(self.avList))
        sel = response.xpath('//div[@class="info"]/ul')
        name = sel.xpath('h3/text()').extract()[0]
        aid = sel.xpath('li[3]/h6[1]/text()').extract()[0]
        lang = sel.xpath('li[4]/h6[1]/text()').extract()[0]
        img = response.xpath('//div[@class="tp"]/img/@src').extract()[0]
        if 'http:' in img:
            pass
        else:
            img = 'http:' + img
        # print(name)
        # print(aid) 
        # print(lang) 
        # print(img)
        actor = '';
        for l in sel.xpath('li[1]/a'):
            # print(l.xpath('text()').extract()[0])
            try:
                act = l.xpath('text()').extract()[0]
            except:
                continue
            if act:
                actor = actor + ',' + act  
        actor = actor[1:]

        label = ''
        for l in sel.xpath('li[2]/a'):
            try:
                lab = l.xpath('text()').extract()[0]
            except:
                continue
            if lab:
                label = label + ',' + lab
        
        label = label[1:]

        item['name'] = name
        item['aid'] = aid
        item['lang'] = lang
        item['image_url'] = img
        item['actor'] = actor
        item['label'] = label
        # print(actor)
        # print(label)

        yield item