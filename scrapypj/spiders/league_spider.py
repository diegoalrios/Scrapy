import scrapy


class League_Spider(scrapy.Spider):
    ##vars
    name = 'league'
    start_urls = [
        'https://www.leagueofgraphs.com/es/rankings/summoners/lan'
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
    def parse_players(self, response, **kwargs):  ## **desempaquetar dict
        pass

    def parse(self, response):
        ## console: scrapy crawl scrape -o top.csv [.json etc]
        pass

''' 
    ##crea un archivo html con la response
    def parse(self,response):
        with open('response.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
'''
