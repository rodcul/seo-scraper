import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from securedge.items import SecuredgeItem

class MySpider(CrawlSpider):
    name = 'nofollow'
    # allowed_domains = ['www.securedgenetworks.com']
    # start_urls = ['https://www.securedgenetworks.com/']
    allowed_domains = ['www.securedgenetworks.com']
    start_urls = ['https://www.securedgenetworks.com/']

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # def parse_links(self, response):
    #     items = []
    #     extractor = LinkExtractor(canonicalize=True, unique=True, allow=r'www\.securedgenetworks\.com/\d+')
    #     for link in extractor.extract_links(response):
    #         item = LattesItem()
    #         item['url'] = link.url


    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url and link.nofollow == True:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = SecuredgeItem()
                # item['nofollow'] = link.nofollow
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        # Return all the found items
        return items
