import requests as rq
from bs4 import BeautifulSoup
from service.ptt_option import analysis, op

future = "https://tw.screener.finance.yahoo.net/future/aa02"
foreignFuture = "https://tw.stock.yahoo.com/"
pttOp = "https://www.ptt.cc/bbs/Option/M.1604641504.A.94E.html"


def get_pttop_html():
    response = rq.get(pttOp)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.body.find_all('div', class_='push')
    count = len(body)
    i = 0
    if count >= 40:
        i = count - 40

    result = ""
    while i < count:
        div = body[i]
        result += f"{div.find('span', class_='push-ipdatetime').text.strip()}" \
                  f"[{div.find('span', class_='f3 hl push-userid').text.strip()}]" \
                  f"{div.find('span', class_='f3 push-content').text.strip().replace(': ', ' ')}\n"
        i += 1

    print(result)
    # write_html(body)


def get_future_html():
    response = rq.get(foreignFuture)
    soup = BeautifulSoup(response.text, "html.parser")
    write_html(soup.body)

    # body = soup.find("div", {"id": "ystkfutb"}).div.tbody
    # tr1 = body.tr
    # tr2 = tr1.next_sibling.next_sibling
    #
    # main1 = "{0}: {1} ({2} {3})".format(tr1.th.a.string,
    #                                  tr1.td.string,
    #                                  "▼" if tr1.td.next_sibling.next_sibling.i.string == "跌" else "▲",
    #                                  tr1.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string)
    #
    # main2 = "{0}: {1} ({2} {3})".format(tr2.th.a.string,
    #                                  tr2.td.string,
    #                                  "▼" if tr2.td.next_sibling.next_sibling.i.string == "跌" else "▲",
    #                                  tr2.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string)
    #
    # print(main1)
    # print(main2)


def write_html(html):
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
    '''.format(html)
    f = open("parser/index.html", "w", encoding='utf-8')
    f.write(template)
    f.close()


if __name__ == '__main__':
    print(analysis())
