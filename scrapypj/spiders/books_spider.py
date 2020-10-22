import scrapy

class Books_Spider(scrapy.Spider):
    ##vars
    name = 'books'
    start_urls = [
        'https://books.toscrape.com/'
    ]

    ##methods
    def parse_link_books(self, response, **kwargs):

        title = response.xpath('').get()
        value = response.xpath('').get()
        category = response.xpath('').get()

    def parse(self, response):
        list_books_links = response.xpath('//ol[@class="row"]//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]//div[@class="image_container"]/a/@href').getall()
        next_btn_link =  response.xpath('//ul[@class="pager"]//li[@class="next"]//a/@href').get()

        for link in list_books_links:
            yield response.follow(link,callback=self.parse_link_books)

        if next_btn_link:
            yield response.follow()
        else:
            pass