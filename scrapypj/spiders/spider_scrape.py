import scrapy


class Spider_Scrape(scrapy.Spider):

    ##vars
    name = 'scrape'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    '''
    ##de esta forma demos formato al comando scrapy crowl scrape
    custom_settings = {
        'FEED_URI' : 'autores.csv',
        'FEED_FORMAT' : 'csv',
        'CONCURRENT_REQUESTS':24
        'FEED_EXPORT_ENCODING:'utf-8''
    }   
    
    '''


    ##methods
    def parse_autores(self, response, **kwargs):## **desempaquetar dict

        if kwargs:
            autores=kwargs['autores']

        autores.extend(response.xpath('//div[@class="quote"]//span/small[@class="author"]/text()').getall())
        next_page = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_autores, cb_kwargs={'autores': autores})
        else:
            yield {
                'autores': autores
            }

    def parse(self, response):
        ## console: scrapy crawl scrape -o top.csv [.json etc]
        autores = response.xpath('//div[@class="quote"]//span/small[@class="author"]/text()').getall()
        top = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

        ##retornamosn un dicct
        yield {
            'top': top,
        }
        next_page = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_autores, cb_kwargs={'autores': autores})





    ''' 
    ##crea un archivo html con la response
    def parse(self,response):
        with open('response.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
    '''

