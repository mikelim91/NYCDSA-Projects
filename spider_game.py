from scrapy import Spider, Request
from games.items import GameItem, Field

# //*[@id="chart_body"]/table/tbody//tr[2] #first row

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]

# //*[@id="chart_body"]/table/tbody/tr[2]

# //*[@id="chart_body"]/table/tbody/tr[1]




class SpiderGame( Spider ):
	name = 'spider_game'
	allowed_domains = ["vgchartz.com"]
	start_urls = ["http://www.vgchartz.com/yearly/2006/USA/"]


	def parse(self, response):
		rows = response.xpath('//*[@id="chart_body"]/table/tr')
		# rows = response.xpath('//table[contains(@id,"chart_body")]')

		for row in rows[1:]:
			rank = row.xpath('.//td[1]/text()').extract() # response.xpath('//*[@id="chart_body"]/table//td[1]/text()').extract()
			video_game = row.xpath('.//a/text()').extract() # response.xpath('//*[@id="chart_body"]/table//a/text()').extract()
			console = row.xpath('.//tr/td[2]/text()[1]').extract_first() # response.xpath('//*[@id="new_entry"]//tr/td[2]/text()[1]').extract()
			company_genre = row.xpath('.//text()[2]')[2].extract() # response.xpath('//*[@id="chart_body"]/table//text()[2]')[2].extract() 	
			year = row.xpath('//*[@id="chart_body"]//center/p/a[1]/text()').extract() # response.xpath('//*[@id="chart_body"]//center/p/a[1]/text()').extract()
			weeks_out = row.xpath('.//td[3]/text()').extract() # response.xpath('//*[@id="chart_body"]/table//td[3]').extract()
			yearly_sale = row.xpath('.//td[4]/text()').extract() # response.xpath('//*[@id="chart_body"]/table//td[4]/text()]').extract()
			total_sale = row.xpath('.//td[5]/text()').extract() # response.xpath('//*[@id="chart_body"]/table//td[5]/text()').extract()
			
			# Items
			item = GameItem()
			item['rank'] = rank			
			item['video_game'] = video_game
			item['console'] = console
			item['company_genre'] = company_genre
			item['year'] = year
			item['weeks_out'] = weeks_out
			item['yearly_sale'] = yearly_sale
			item['total_sale'] = total_sale
	
			yield item


			# Page iteration
			country = ['USA','JAPAN','EUROPE','GLOBAL']
			year = range(2006,2019)
			urls = []

			for c in country:
				for y in year:
					urls.append('http://www.vgchartz.com/yearly/'+str(y)+'/'+c+'/')
			for url in urls:
				yield Request(url=url, callback=self.parse)

# class VideoGamesSpider(Spider):
#         # i = 0
#         name = 'videogames_spider'
#         allowed_domains = ['www.metacritic.com']
#         start_urls = ['https://www.metacritic.com/browse/games/score/metascore/all/ps4']
#         def parse(self, response):
#             last_page_num = int(response.xpath('//li[@class="page last_page"]/a/text()').extract_first())
#             page_urls = [f'https://www.metacritic.com/browse/games/score/metascore/all/ps4?sort=desc&page={i}' for i in range(last_page_num)]
#             for url in page_urls[:18]:
#                 yield Request(url=url, callback=self.parse_list_pages)
#         def parse_list_pages(self, response):
#             begin = 'https://www.metacritic.com'
#             game_pages = response.xpath('//ol[@class="list_products list_product_condensed"]//div[@class="basic_stat product_title"]/a/@href').extract()
#             result_urls = [begin + page for page in game_pages]
#             for url in result_urls:
#                 yield Request(url, self.parse_inner_page)


# ['http://www.vgchartz.com/yearly/{}/USA/'.format(x) for x in range(2006,2019) for y in 


# country = ['USA','JAPAN','EUROPE','GLOBAL']
# year = range(2006,2019)
# a = []
# for c in country:
#     for y in year:
#         a.append('http://www.vgchartz.com/yearly/'+str(y)+'/'+c+'/')
# print(a)



# //*[@id="chart_body"]/table//table/tbody/tr/td[2]

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a/br

# //*[@id="chart_body"]/table #row 1 game 1

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2] #table data for game 1

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a #Game Name 

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/text()[1] # game console

# //*[@id="chart_body"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/text()[2] # Game company and Genre

# //*[@id="chart_body"]/table/tbody/tr[2]/td[3] # number of weeks

# //*[@id="chart_body"]/table/tbody/tr[2]/td[4] # yearly sale

# //*[@id="chart_body"]/table/tbody/tr[2]/td[5] # total sales

# //*[@id="chart_body"]/table/tbody/tr[2]/td[1] #position





 #    video_game = scrapy.Field()
 #    genre_tag = scrapy.Field()
 #    weeks_out = scrapy.Field()
 #    yearly_sale = scrapy.Field()
 #    total_sale = scrapy.Field()
 #    rank = scrapy.Field()
 #    platform = scrapy.Field()
 #    platform_yearly = scrapy.Field()
 #    platform_total = scrapy.Field()





	##Creating a parse method for every single page
	# def parse( self, resepones) :
	# 	begin = 'http://www.vgchartz.com/yearly/'
	# 	end = '/USA/'vgchartz.com
	# 	next_urls = [begin + end] + [begin + '20%d'%pgn +  end for pgn in range(6,npages+1)]
	# 	npages = int(response.xpath('//li[@class="page-item"]//text()').extract()[-1])

	# 	for url in next_urls:
	# 		yield scrapy.Request(url,self.parse_list_page) #scrape url and parse with self.parse_list_page method
	# def parse_list_page(self,response): #parsing method 
	# 	print(response)
	# 	print("=" * 50)
	# 	pass

