import scrapy

from Seebug.items import SeebugItem

'''
运行爬虫
scrapy crawl SeebugSpider  
'''


class SeebugspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'SeebugSpider'
    # 允许的域名
    allowed_domains = ['paper.seebug.org']
    # 入口 URL,扔到调度器里面
    start_urls = ['http://paper.seebug.org/?page=1']

    def parse(self, response):
        # print(response.text)
        Article_Infos = response.xpath('//*[@id="wrapper"]/main/div/article')
        for i_term in Article_Infos:
            # print(i_term)
            seebug_iterm = SeebugItem()

            seebug_iterm['Article_Title'] = i_term.xpath("./header/h5/a/text()").extract()
            # print(seebug_iterm['Article_Title'])
            for i_title in seebug_iterm['Article_Title']:
                seebug_iterm['Article_Title'] = i_title
                # print(i_title)

            seebug_iterm['Article_Link'] = i_term.xpath('./header/h5/a/@href').extract()
            for i_link in seebug_iterm['Article_Link']:
                i_link = "https://paper.seebug.org" + i_link
                seebug_iterm['Article_Link'] = i_link.rstrip()
                # print(i_link)

            seebug_iterm['Article_Time'] = i_term.xpath('./header/section/span/time[@class="timeago"]/text()').extract()
            for i_time in seebug_iterm['Article_Time']:
                seebug_iterm['Article_Time'] = i_time.lstrip()

                # print(i_time)

            seebug_iterm['Article_Tag'] = i_term.xpath('.//header/section/a/text()').extract()
            for i_tag in seebug_iterm['Article_Tag']:
                seebug_iterm['Article_Tag'] = i_tag
                # print(i_tag)

            # seebug_iterm['Article_Introduction'] = i_term.xpath('./section/text()').extract()
            Introduction = i_term.xpath('./section/text()').extract()
            for i_introduction in Introduction:
                # ''' ['', '      译者：知道创宇404翻译组', '原文链接：https://blog.sonatype.com/bladabindi-njrat-rat-in-jdb.js-npm-malware', '在感恩节周末，我们...'] '''
                data = i_introduction.split('\n')

                for info in data:
                    if "作者" in info or "译者" in info :
                        seebug_iterm['Article_Author'] = info.lstrip().rstrip()

                    if "原文链接" in info or "原文来自" in info:
                        print("info="+info)
                        # if '：' in info:
                        #     i_orign_link_name = info.split("：")[0]
                        #     i_orign_link = info.split("：")[1]
                        # else:
                        #     i_orign_link_name = info.split("：")[0]
                        #     i_orign_link = info.split":")[1] + info.split(":")[1]

                        seebug_iterm['Article_Origin_Link'] = info.lstrip()
                    if "译者" not in info and "作者" not in info and "原文链接" not in info and "原文来自" not in info and "    " not in info:
                        seebug_iterm['Article_Summary'] = info

                # print(i_author + " =>> " + i_orign_link_name + " =>> " + i_orign_link + " =>> " + i_summary)
            print(seebug_iterm)
            yield seebug_iterm
        next_link = response.xpath('//*[@id="wrapper"]/main/div/nav/a[@class="older-posts"]/@href').extract()
        if next_link:
            next_link=next_link[0]
            print("https://paper.seebug.org/" + next_link)
            yield scrapy.Request("https://paper.seebug.org/"+next_link, callback=self.parse)

        # pass
