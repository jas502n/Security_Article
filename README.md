# Security_Article
scrapy website Article and link ...

e.g.

`pip3 install lxml,scrapy`

```
文章标题 Article_Title
//*[@id="wrapper"]/main/div/article/header/h5/a/text()

//*[@id="wrapper"]/main/div/article/header/h5/a

文件链接 Article_Link
//*[@id="wrapper"]/main/div/article/header/h5/a/@href

文章时间 Article_Time
//*[@id="wrapper"]/main/div/article/header/section/span/time[1]

文章标签 Article_Tag
//*[@id="wrapper"]/main/div/article/header/section/a

文章简介 Article_Introduction
//*[@id="wrapper"]/main/div/article/section/text()

下一页
//*[@id="wrapper"]/main/div/nav/a[@class="older-posts"]/@href[2]
```

`scrapy crawl SeebugSpider -o seebug.csv`

```
{
	'Article_Author': '译者：知道创宇404实验室翻译组',
	'Article_Link': 'https://paper.seebug.org/1230/',
	'Article_Origin_Link': '原文链接：Cycldek: Bridging the (air) gap ',
	'Article_Summary': '在调查关于Cycldek组织2018年后有关攻击活动时，发现对该组织的...',
	'Article_Tag': '威胁情报',
	'Article_Time': '2020年06月04日',
	'Article_Title': '卡巴斯基报告：针对 Cycldek 黑客组织知识鸿沟的相关信息'
}
```
![](./images/seebug.png)
