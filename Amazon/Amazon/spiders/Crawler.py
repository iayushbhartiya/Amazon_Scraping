import scrapy
from ..items import AmazonItem
from scrapy.spidermiddlewares.httperror import HttpError




class amazon_com(scrapy.Spider):
    name = 'amazon'

    def start_requests(self):
        # Using Excel I've concatenated all the cell to find array of ASIN and country
        asin = ["1015", "1015", "000004458X", "000004458X", "1002198", "1002198", "1002791", "1002791", "1002864",
                "1002864", "1003704", "1003704", "1003763", "1003763", "1004271", "1004271", "000101742X", "000101742X",
                "1017519", "1017519", "000102163X", "000102163X", "1022369", "1022369", "1022857", "1022857", "1032666",
                "1032666", "1034677", "1034677", "1034936", "1034936", "1034944", "1034944", "1035002", "1035002",
                "1035029", "1035029", "1035053", "1035053", "1035053", "1035339", "1035339", "1036866", "1036866",
                "1036866", "1037137", "1037137", "1037188", "1037188", "1037994", "1037994", "000103863X", "000103863X",
                "1039466", "1039466", "1040871", "1040871", "1040979", "1040979", "1040987", "1040987", "1041002",
                "1041002", "1041991", "1041991", "000104317X", "000104317X", "1043331", "1043331", "000104348X",
                "000104348X", "1043498", "1043498", "1043773", "1043773", "000104396X", "000104396X", "1048325",
                "1048325", "1049119", "1049119", "1057774", "1057774", "1057790", "1057790", "1057790", "1057812",
                "1057812", "1057812", "1057987", "1057987", "1059238", "1059238", "1060619", "1060619", "1060694",
                "1060694", "1060694", "1061305", "1061305", "1063685", "1063685", "1065440", "1065440", "1065548",
                "1065548", "1066544", "1066544", "1067087", "1067087", "1067311", "1067311", "000106875X", "000106875X",
                "000106875X", "1069470", "1069470", "1070991", "1070991", "000107119X", "000107119X", "1072064",
                "1072226", "1072226", "1072250", "1072250", "1072498", "1072498", "1073389", "1073389", "1073915",
                "1073915", "1074504", "1074504", "1074954", "1074954", "1075691", "1075691", "1075969", "1075969",
                "1075977", "1075977", "1077619", "1077619", "1077732", "1077732", "1077988", "1077988"]

        country = [
            "de", "fr", "de", "fr", "de", "fr", "fr", "it", "de", "fr", "de", "fr", "de", "fr", "fr", "it", "de", "fr",
            "de", "fr", "de", "fr", "fr", "it", "fr", "it", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr",
            "de", "fr", "de", "es", "fr", "de", "fr", "de", "es", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr",
            "de", "fr", "fr", "it", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr",
            "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "es", "fr", "de", "es", "fr",
            "de", "fr", "de", "fr", "de", "fr", "de", "es", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de",
            "fr", "de", "fr", "de", "fr", "es", "fr", "it", "de", "fr", "de", "fr", "de", "fr", "de", "de", "fr", "de",
            "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de", "fr", "de",
            "fr", "de", "fr", "de", "fr"]
        # creating list of URLs
        start_urls = []

        for i in range(len(asin)):
            a = f"https://www.amazon.{country[i]}/dp/{asin[i]}"
            start_urls.append(a)
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.error_404 )
    # parsing items

    def parse(self,response):
        prod = AmazonItem()

        title = response.css("[id = 'productTitle']::text").extract_first()
        img_url = response.css("[id = 'img-wrapper'] img::attr(src)").extract_first()
        price = response.css('span.a-color-base span::text').extract_first()

        prod['title'] = title
        prod['img_url'] = img_url
        prod['price'] = price

        yield prod

    def error_404(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('%s Unavailabe ', response.url)













