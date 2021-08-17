def parse(response):
    Data=response.xpath('//ul[@class="menutop"]/li')
    for row in Data:
        LINK=row.xpath('.//a/@id').get()
        if LINK!='ActiveMenu0':
            ID=LINK.replace('ActiveMenu','')
            Page=1
            url='https://vneconomy.vn/timeline/'+ID+'/trang-'+str(Page)+'.htm'
            yield scrapy.Request(url,callback=self.parse_list,meta={'ID':ID,'Page':Page})
    pass

def parse_list(response):
    ID=response.meta['ID']
    Page=response.meta['Page']+1
    LINKS=response.xpath('//article//h2/a/@href').getall()
    for url in LINKS:
        yield scrapy.Request(url,callback=self.parse_content)


parse("https://vneconomy.vn/")