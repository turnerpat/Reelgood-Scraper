"""
# Patrick Turner
# reelgood spider
# version 2.1

    A scrapy web scraper for reelgood.com.

    Usage - use python interpreter to navigate to ~/reelgoodSpider/reelgoodSpider/spiders/ and run spider with:
        scrapy runspider reelgood.py -o reelgood.jsonl -t jsonlines
    You may change the output file to different type. Output file will be placed in the spiders directory.

    Change the offset variable below to adjust how many tv and movie pages are being scraped. See comments for more
    details.

    TV and Movie pages are parsed and have their attributes scraped by the parse_tv and parse_movie methods
    respectively. Attributes scraped include the title, imdb score, reelgood score, list of genre(s), maturity rating,
    release year(s), runtime for movies, number of seasons for tv, the ongoing/finished status of tv shows,
    list of streaming services, list of associated tags, country of production, director of movie,
    top three* billed actors (can be increased, see comments below), link to poster, url, and description
    of plot/critical reception. This is a total of 15 scraped attributes per page.

    A cache of scraped pages will be saved to the directory reelgoodSpider/.scrapy/ by default. WARNING: If left on
    and a large offset index is used a large cache will be generated.

    Other settings for the spider can be accessed and changed via settings.py in the reelgoodSpider directory.
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ReelgoodSpider(CrawlSpider):
    name = 'reelgood'
    allowed_domains = ['reelgood.com']
    # Restrict the offset of the movie and tv lists being crawled (by increments of 50 starting at 0)
    # For example: offset = 0 = 50 links per each list, offset = 1 = 100 links per each list, etc.
    offset = 200
    start_urls = []
    i = 0
    for i in range(offset + 1):
        start_urls.append(f'https://reelgood.com/movies?offset={i * 50}')
        start_urls.append(f'https://reelgood.com/tv?offset={i * 50}')
    rules = [(Rule(LinkExtractor(allow=r'/show/', restrict_xpaths='//body//div[@id="app_mountpoint"]//main'
                                                                  '//div[@itemtype="//schema.org/ItemList"]'),
                   callback='parse_tv', follow=True)),
             (Rule(LinkExtractor(allow=r'/movie/', restrict_xpaths='//body//div[@id="app_mountpoint"]//main'
                                                                   '//div[@itemtype="//schema.org/ItemList"]'),
                   callback='parse_movie', follow=True))]

    def parse_movie(self, response):
        a = {'title': response.xpath('//h1[@itemprop="name"]/text()').extract_first(),
             'imdb': response.xpath('//span[1][@class="css-vyyf4l ey4ir3j1"]//div//div//span/text()')[0].extract(),
             'reelgood': response.xpath('//div[1][@class="css-79elbk e1itp0sf0"]//svg//text/text()')[2].extract(),
             'genre(s)': response.xpath('//span[2][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'rating': response.xpath('//span[3][@class="css-vyyf4l ey4ir3j1"]//span/text()').extract_first(),
             'year': response.xpath('//span[4][@class="css-vyyf4l ey4ir3j1"]/a/text()')[0].extract(),
             'runtime': response.css('span.css-vyyf4l:nth-child(6)::text').extract_first(),
             'streaming': response.xpath('//span[6][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'tags': response.xpath('//span[7][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'country': response.xpath('//span[8][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract_first(),
             'director': response.xpath('//div[@class="css-gq6ll egg5eqo4"]/a/@title').extract_first(),
             # Change the numbers in the array at the end to determine how many actors are shown:
             # (start from 1 to remove director)
             'actors': response.xpath('//div[@class="css-gq6ll egg5eqo4"]/a/@title').extract()[1:4],
             'poster': response.xpath('//img[@itemprop="image"]/@src').extract_first(),
             'url': response.url,
             'mediatype': 'Movie',
             'description': response.xpath('//p[@itemprop="description"]/text()').extract_first()}
        print('URL is: {}'.format(a['url']))
        yield a

    def parse_tv(self, response):
        a = {'title': response.xpath('//h1[@itemprop="name"]/text()').extract_first(),
             'imdb': response.xpath('//span[1][@class="css-vyyf4l ey4ir3j1"]//div//div//span/text()')[0].extract(),
             'reelgood': response.xpath('//div[1][@class="css-79elbk e1itp0sf0"]//svg//text/text()')[2].extract(),
             'genre(s)': response.xpath('//span[2][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'rating': response.xpath('//span[3][@class="css-vyyf4l ey4ir3j1"]//span/text()').extract_first(),
             'year(s)': response.xpath('//span[4][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract_first() +
                        response.xpath('//span[4][@class="css-vyyf4l ey4ir3j1"]/text()').extract_first(),
             'seasons': response.css('span.css-vyyf4l:nth-child(6)::text').extract_first(),
             'status': response.css('span.css-vyyf4l:nth-child(7)::text').extract_first(),
             'streaming': response.xpath('//span[7][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'tags': response.xpath('//span[8][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract(),
             'country': response.xpath('//span[9][@class="css-vyyf4l ey4ir3j1"]/a/text()').extract_first(),
             # Change the numbers in the array at the end to determine how many actors are shown:
             'actors': response.xpath('//div[@class="css-gq6ll egg5eqo4"]/a/@title').extract()[0:3],
             'poster': response.xpath('//img[@itemprop="image"]/@src').extract_first(),
             'url': response.url,
             'mediatype': 'TV',
             'description': response.xpath('//p[@itemprop="description"]/text()').extract_first()}
        print('URL is: {}'.format(a['url']))
        yield a
