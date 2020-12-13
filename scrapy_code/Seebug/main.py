from scrapy import cmdline

cmdline.execute("scrapy crawl SeebugSpider -o seebug.csv".split())