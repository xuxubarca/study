#引入文件
import scrapy

class CourseItem(scrapy.Item):

    # 名称
    name = scrapy.Field()

    # 图片
    image_url = scrapy.Field()

    # ID
    aid = scrapy.Field()

    # 演员
    actor = scrapy.Field()

    # 标签
    label = scrapy.Field()

    # 语言
    lang = scrapy.Field()

    #图片地址
    image_path = scrapy.Field()