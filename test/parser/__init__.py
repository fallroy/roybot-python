import requests as rq
from bs4 import BeautifulSoup

future = "https://tw.screener.finance.yahoo.net/future/aa02"
foreignFuture = "https://tw.stock.yahoo.com/"

response = rq.get(future)  # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text  # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "html.parser")  # 指定 lxml 作為解析器
body = soup.find("div", {"id": "ystkfutb"}).div.tbody
tr1 = body.tr
tr2 = tr1.next_sibling.next_sibling

main1 = "{0}:{1} {2} {3}".format(tr1.th.a.string,
                                 tr1.td.string,
                                 tr1.td.next_sibling.next_sibling.i.string,
                                 tr1.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string)

main2 = "{0}:{1} {2} {3}".format(tr2.th.a.string,
                                 tr2.td.string,
                                 tr2.td.next_sibling.next_sibling.i.string,
                                 tr2.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string)

htmlString = body.prettify()
print(main1)
print(main2)

template = '''<!DOCTYPE html>
<html lang="en">
    <head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
{0}
</body>
</html>
'''.format(htmlString)
f = open("parser/index.html", "w", encoding='utf-8')
f.write(template)
f.close()
