# Gov Crawler

## 简介 

一个基于scrapy的爬虫项目，全站采集所有数据，并将其关系储存到mongoDB中。

## 使用

1. 安装好python依赖，docker
	- `pip3 install -r requirements.txt`
	- `curl -sSL https://get.docker.com/ | sh`

2. 请配置settings.py中的以下变量：
	- `DATA_DIR` 一个目录，将保存所有采集数据
	- `DOMAINS_LIST` 需要采集的站点的列表，支持`txt`格式或`xls`
	- `MONGO_DB` mongoDB数据库的名字，它将保存所有资源关系

3. 启动splash，启动redis，配置好mongoDB

4. 启动scrapy：`scrapy crawl gov`

