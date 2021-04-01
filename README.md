# 简易的Issuu爬虫基于Scrapy框架
## 使用说明
* Issuu-spider目录下运行 'alex' 是我的爬虫名
```bash
scrapy crawl alex
```
* 改动位置
state_code 和 start_urls
  
检查网页 -> 网络 -> XHR里有个 master-70?xx
```
master-70?state=Kb37l2wNAVkOEEW_70FHjzjTWVJRjCUuoK59Lac8mt7okzZkJPl5yqH--U4Cdtc4kSWMoLND1SGzqxkl6X1zi9mNZ97Fv_ux8dPmG0LS1zBkGlc6fGXSY35_vX9rnl7ojoImVlwsiwFeQAliKzlcUQfbLoqQN6MyUWgvB7FIY8SEROh3izzvPze3DB2uJQ==&pageSize=20&format=json
```
从里头复制黏贴所需信息到爬虫