import scrapy
from tutorial.items import TutorialItem

"""
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
"""


class ImageSpider(scrapy.Spider):
    name = "image_spider"
    
    start_urls = [
                  "http://www.decormatters.com/index.php",
                  ]
        
    def parse(self, response):
        for elem in response.xpath("//img"):
          img_url = elem.xpath("@src").extract_first()
          list_a = response.urljoin(img_url)
          yield TutorialItem(image_urls=[list_a])
