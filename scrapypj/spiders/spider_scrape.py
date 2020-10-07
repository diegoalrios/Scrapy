import scrapy

class Spider_Scrape(scrapy.Spider):

    ##vars
    name = 'scrape'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    ##methods

    def parse(self, response):
        ## console: scrapy crawl scrape -o top.csv [.json etc]
        topten = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        ##retornamosn un dicct
        yield {
            'top_ten' : topten,
        }


    ''' 
    ##crea un archivo html con la response
    def parse(self,response):
        with open('response.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
    '''

