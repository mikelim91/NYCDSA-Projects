from scrapy import Spider, Request
from games.items import GameItem, Field


class SpiderGame( Spider ):
	name = 'spider_game'
	allowed_domains = ["vgchartz.com"]

	# start_urls = ["http://www.vgchartz.com/yearly/2006/Japan/"]
	# start_urls = ["http://www.vgchartz.com/yearly/2006/USA/"]
	# start_urls = ["http://www.vgchartz.com/yearly/2006/Global/"]
	# start_urls = ["http://www.vgchartz.com/yearly/2006/Europe/"]
	# start_urls = ["http://www.vgchartz.com/yearly/2006/Global/"]

	# start_urls = ["http://www.vgchartz.com/weekly/38396/Japan/"]
	start_urls = ["http://www.vgchartz.com/weekly/38396/USA/"]
	# start_urls = ["http://www.vgchartz.com/weekly/38396/Global/"]
	# start_urls = ["http://www.vgchartz.com/weekly/38396/Europe/"]
	# start_urls = ["http://www.vgchartz.com/weekly/38396/Global/"]

	def parse(self, response):
		rows = response.xpath('//*[@id="chart_body"]/table/tr')
		# rows = response.xpath('//table[contains(@id,"chart_body")]')

		for row in rows[1:]:
			rank = row.xpath('.//td[1]/text()').extract_first() # response.xpath('//*[@id="chart_body"]/table//td[1]/text()').extract()
			video_game = row.xpath('.//a/text()').extract_first() # response.xpath('//*[@id="chart_body"]/table//a/text()').extract()
			console = row.xpath('.//tr/td[2]/text()[1]').extract_first() # response.xpath('//*[@id="new_entry"]//tr/td[2]/text()[1]').extract_first()
			company_genre = row.xpath('.//text()[2]')[2].extract() # response.xpath('//*[@id="chart_body"]/table//text()[2]')[2].extract() 	
			year = row.xpath('//*[@id="chart_body"]//center/p/a[1]/text()').extract_first() # response.xpath('//*[@id="chart_body"]//center/p/a[1]/text()').extract()
			weeks_out = row.xpath('.//td[3]/text()').extract_first() # response.xpath('//*[@id="chart_body"]/table//td[3]').extract()
			yearly_sale = row.xpath('.//td[4]/text()').extract_first() # response.xpath('//*[@id="chart_body"]/table//td[4]/text()]').extract()
			total_sale = row.xpath('.//td[5]/text()').extract_first() # response.xpath('//*[@id="chart_body"]/table//td[5]/text()').extract()
			country = row.xpath('//*[@id="chart_body"]//tr[3]/td[1]/a/text()').extract_first() # USA response.xpath('.//*[@id="chart_body"]//tr[3]/td[1]/a/text()').extract()
			# country = row.xpath('//*[@id="chart_body"]//tr[3]/td[3]/a/text()').extract_first() # JAPAN response.xpath('.//*[@id="chart_body"]//tr[3]/td[3]/a/text()').extract()
			# country = row.xpath('//*[@id="chart_body"]//tr[3]/td[2]/a/text()').extract_first() # EUROPE response.xpath('.//*[@id="chart_body"]//tr[3]/td[2]/a/text()').extract()
			# country = row.xpath('//*[@id="chart_body"]//tr[2]/td/a/text()').extract_first() # GLOBAL response.xpath('.//*[@id="chart_body"]//tr[2]/td/a/text()').extract()


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
			item['country'] = country
			yield item


			# Page iteration by each country
			# country = ['Japan']
			# country = ['USA'] 
			# country = ['Global']
			# country = ['Europe']
			
			country = ['USA','Europe','Japan','Global']
			urls = []
			
			#weekly
			# year = range(38396,38985,7) # feb 12 2005 (38396) - > dec 29 2018 (43464)
			
			
			# for c in country:
			# 	for y in year:
			# 		urls.append('http://www.vgchartz.com/weekly/'+str(y)+'/'+c+'/')
			# for url in urls:
			# 	yield Request(url=url, callback=self.parse)

			# yearly
			year = range(2006,2019) # feb 12 2005 (38396) - > dec 29 2018 (43464)

			for c in country:
				for y in year:
					urls.append('http://www.vgchartz.com/yearly/'+str(y)+'/'+c+'/')
			for url in urls:
				yield Request(url=url, callback=self.parse)


			# Weekly 
			# country = ['USA','JAPAN','EUROPE','GLOBAL']
			# year = range(38396,43464)
			# a = []
			# for c in country:
			#     for y in year:
			#         a.append('http://www.vgchartz.com/yearly/'+str(y)+'/'+c+'/')
			# for url in urls:
			# 	yield Request(url=url, callback=self.parse)



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


