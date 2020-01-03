# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import os
# from urllib import request
#
# """ 这个是传统的方式"""
#
# #需要是，在项目中的根目录创建一个images文件夹来保存所有图片，每一个分类在images文件夹中，又单独创建一个所属分类的文件夹，把对应的图片下载到对应的分类中
# #用os.path.dirname()去获取相应的文件夹，判断有没有创建，没有就自带创建，再用os.path.join()方法，把文件夹/文件夹和文件拼接起来
# class AudiPipeline(object):
#
#     def __init__(self):
#
#         #获取images文件夹的路径是在根目录,最里面获取的路径是pipeline文件的目录，所以还需要往上一层获取
#         self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
#
#         #判断images文件夹是否存在，不存在就创建
#         if not os.path.exists(self.path):
#             os.mkdir(self.path)
#
#     def process_item(self, item, spider):
#
#         #提取分类
#         category =  item['category']
#         #提取图片的urls
#         urls = item['urls']
#
#         #同样做一个判断，每一个分类是否存在文件夹，没有就创建
#         category_path = os.path.join(self.path,category)
#         if not os.path.exists(category_path):
#             os.mkdir(category_path)
#
#         #遍历所有的urls，进行下载，这里面会有个细节需要考虑，下载的图片要有个名字，因此我们需要提取图片的名字出来
#         for url in urls:
#             #获取图片名称,发现所有图片名称(图片url)的区别在于最后一个下划线"_"后面的值不同,使用split()切割就行了
#             image_name = url.split('_')[-1]
#
#             #下载图片，同时也把文件夹和文件名拼接起来
#             request.urlretrieve(url,os.path.join(category_path,image_name))
#
#         return item


"""

    因为利用scrapy自带的ImagePipeline方法，可以快速的下载存储图片，但是都是保存在同一个文件夹下，没有按照分类保存，不满足我们的需求，因此，需要重写这个pipeline的部分方法

"""

import os
from Audi.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline


class Audi_RS5Pipeline(ImagesPipeline):  #继承的父类是ImagesPipeline

    #但是，好像这个函数也是无法修改有分类文件夹的问题，因为它没有category参数调用，需要找到调用item的方法，才能调用category,在源码中，再次寻找可以操作item的方法
    def get_media_requests(self, item, info):          #这个方法最终的调用方法是：DEFAULT_IMAGES_URLS_FIELD = 'image_urls'    ，也就是我们在item设置的image_urls，然后通过request方法，去请求下载这个列表里面的所有图片
        #这个方法是在发送下载请求前调用，其实这个方法本身就是去发送下载请求的，是一个请求列表
        request_downloads = super(Audi_RS5Pipeline, self).get_media_requests(item,info)   #重写方法

        for request_download in request_downloads:
            request_download.item = item

        return request_downloads

    #因为最后保存的图片都是在full文件夹下，因此我们需要重写它,根据关键字full文件夹找到相应源码对应的方法
    def file_path(self, request, response=None, info=None):
        #这个方法是在图片将要存储的时候调用，来获取这个图片存储的路径
        path = super(Audi_RS5Pipeline, self).file_path(request,response=None,info=None)  #重写方法

        #然后根据上面重写的方法，返回的request请求，我们可以通过request请求获取item下的分类category
        category = request.item.get('category')      #request请求的一个方法：[Request(x) for x in item.get(self.images_urls_field, [])]

        #存储的路径
        image_store = IMAGES_STORE

        #拼接文件夹路径
        category_path = os.path.join(image_store,category)
        #判断分类文件夹是否存在
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        #获取图片的文件名,源代码的文件名的方式是这样的：'full/%s.jpg' % (image_guid) ，full是文件夹
        image_name = path.replace(r'full/','')

        #最后拼接分类和图片文件
        image_path = os.path.join(category_path,image_name)

        return image_path

#最后记得，setting文件中的Pipeline文件开启，而且需要用到我们重写的Pipeline

