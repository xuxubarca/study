import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class ImgPipeline(ImagesPipeline):
    #通过抓取的图片url获取一个Request用于下载
    def get_media_requests(self, item, info):
        #返回Request根据图片图片url下载
        yield scrapy.Request(item['image_url'],meta={'item':item})
    #当下载请求完成后执行该方法
    def item_completed(self, results, item, info):
        #获取下载地址
        image_path = [x['path'] for ok, x in results if ok]
        #判断是否成功
        if not image_path:
            raise DropItem("Item contains no images")
        #将地址存入item
        item['image_path'] = image_path
        return item


    def file_path(self,request,response=None,info=None):
        item = request.meta['item']
        image_guid = item['aid']+'.'+request.url.split('/')[-1].split('.')[-1]
        filename = u'full/{0}/{1}'.format('lhav', image_guid)
        return filename
