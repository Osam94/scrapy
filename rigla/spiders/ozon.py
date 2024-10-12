import scrapy


class OzonSpider(scrapy.Spider):
    name = "ozon"
    allowed_domains = ["www.ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/zhenskaya-odezhda-7501/"]

    def parse(self, response):
        
        names = response.xpath("//div/span[@class='tsBody500Medium']")
        extracted_names = set()
        for name in names:
            name_text = name.xpath(".//text()").get()
            if name_text not in extracted_names:
                extracted_names.add(name_text)
        yield {"name": extracted_names}
