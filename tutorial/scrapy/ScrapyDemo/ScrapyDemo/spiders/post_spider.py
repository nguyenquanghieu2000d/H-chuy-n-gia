import os

import scrapy


class PostSpider(scrapy.Spider):
    filePath = "ScrapyDemo/data"
    fileName = "vneconomy"
    type = "html"
    name = "posts"
    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ['https://vneconomy.vn/tieu-diem.htm?trang=' + str(i) for i in range(1, 101)]

    def parse(self, response, **kwargs):
        page = response.url.split("=")[-1]
        filename = os.path.join(self.filePath, self.fileName + str(page) + "." + self.type)
        print(filename)
        with open(filename, "wb") as f:
            f.write(response.body)
        pass

    pass
