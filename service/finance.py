import requests as rq
from bs4 import BeautifulSoup

future = "https://tw.screener.finance.yahoo.net/future/aa02"


def rp():
    response = rq.get(future)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find("div", {"id": "ystkfutb"}).div.tbody
    tr1 = body.tr
    tr2 = tr1.next_sibling.next_sibling

    result = "{0}: {1} ({2} {3})\n{4}: {5} ({6} {7})" \
        .format(tr1.th.a.string,
                tr1.td.string,
                "▼" if tr1.td.next_sibling.next_sibling.i.string == "跌" else "▲",
                tr1.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string,
                tr2.th.a.string,
                tr2.td.string,
                "▼" if tr2.td.next_sibling.next_sibling.i.string == "跌" else "▲",
                tr2.td.next_sibling.next_sibling.next_sibling.next_sibling.span.string)

    return result
