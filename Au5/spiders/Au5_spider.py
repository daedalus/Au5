from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from Au5.items import Au5Item

class Au5Spider(BaseSpider):

    	name = 'Au5'
    	allowed_domains = ['labanca.com.uy']
   	start_urls = ['http://www3.labanca.com.uy/estadisticas/cincodeoro']

	def parse(self, response):
       		hxs = HtmlXPathSelector(response)
       		sites = hxs.select('//ul[@class="cinco"]')
       		items = []
       		
		cat = 0
		for site in sites:
           		balls = site.select('li/img/@alt').extract()
           		stats = site.select('li/span/text()').extract()
			cat = cat + 1
			
			for ball,stat in zip(balls,stats):
				item = Au5Item()
				item['ball'] = ball
				item['stat'] = stat
				item['cat'] = cat
           			items.append(item)


       		return items

