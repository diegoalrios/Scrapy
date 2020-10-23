import scrapy

class Books_Spider(scrapy.Spider):
    ##vars
    name = 'books'
    start_urls = [
        'https://books.toscrape.com/'
    ]

    ##methods
    def parse_link_books(self, response, **kwargs):

        title = response.xpath('//div[@class="col-sm-6 product_main"]//h1/text()').get()
        value = response.xpath('//div[@class="col-sm-6 product_main"]//p[@class="price_color"]/text()').get()
        stok = response.xpath('//div[@class="col-sm-6 product_main"]//p[@class="instock availability"]/text()').getall()
        yield {
            'title': title,
            'value': value,
            'stok' : stok[1]
        }

    def parse(self, response):
        list_books_links = response.xpath('//ol[@class="row"]//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]//div[@class="image_container"]/a/@href').getall()
        next_btn_link =  response.xpath('//ul[@class="pager"]//li[@class="next"]//a/@href').get()

        for link in list_books_links:

            yield response.follow(link,callback=self.parse_link_books)

        if next_btn_link:

            yield response.follow(next_btn_link,callback=self.parse)
