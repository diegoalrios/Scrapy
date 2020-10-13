import scrapy
##ruta:

class League_Spider(scrapy.Spider):
    ##vars
    name = 'league'
    start_urls = [
        'https://www.leagueofgraphs.com/es/rankings/summoners/lan'
    ]

    ##methods
    def parse_link_players(self, response, **kwargs):
        print("2" * 100)
        if kwargs:
            list_players_link=kwargs['list_player_link']

        list_players_link.extend(response.xpath('//div[contains(@class, "box-padding-10")]//table/tr/td/a[starts-with(@href, "/summoner")]/@href').getall())

        list_button_link = response.xpath('//ul[@class="pagination"]/li/a[@href]/@href').getall()
        list_view_button_link = response.xpath('//ul[@class="pagination"]/li/a[@href]/text()').getall()
        next_buton = None

        if len(list_button_link) == len(list_view_button_link):
            for i in range(len(list_view_button_link)):
                if list_view_button_link[i] == '>':
                    next_buton = list_button_link[i]



        if next_buton:
            yield response.follow(next_buton, callback=self.parse_link_players,cb_kwargs={'list_player_link': list_players_link})

    def parse(self, response):
       list_players_link=response.xpath(
           '//div[contains(@class, "box-padding-10")]//table/tr/td/a[starts-with(@href, "/summoner")]/@href').getall()
       list_button_link=response.xpath('//ul[@class="pagination"]/li/a[@href]/@href').getall()
       list_view_button_link=response.xpath('//ul[@class="pagination"]/li/a[@href]/text()').getall()
       next_buton=None

       if len(list_button_link) == len(list_view_button_link):
           for i in range(len(list_view_button_link)):
               if list_view_button_link[i]=='>':
                   next_buton=list_button_link[i]

       if next_buton:
           print(next_buton)
           print("1"*100)
           yield response.follow(next_buton, callback=self.parse_link_players, cb_kwargs={'list_player_link': list_players_link})