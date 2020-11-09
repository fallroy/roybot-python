import requests as rq
from bs4 import BeautifulSoup

future = "https://www.ptt.cc/bbs/Option/M.1604641504.A.94E.html"
famousPerson = ""
rise = ["救多", "假崩", "假摔", "誘空", "軋", "漲", "噴", "頂"]
down = ["空軍日", "下去", "下山", "爆崩", "救空", "誘多", "崩", "跌"]
unknown = []


def op():
    data_list = _get_data()
    count = len(data_list)
    i = 0
    if count >= 50:
        i = count - 50

    result = ""
    while i < count:
        data = data_list[i]
        result += f"{data[0]}[{data[1]}] {data[2]}\n"
        i += 1
    return result


def analysis():
    result = [0, 0]
    data_list = _get_data()
    for div in data_list:
        for r in rise:
            if div[2].find(r) > -1:
                result[0] += 1
                print("Rise: {0}:{1}".format(div[1], div[2]))
                break

        for r in down:
            if div[2].find(r) > -1:
                result[1] += 1
                print("Down: {0}:{1}".format(div[1], div[2]))
                break

    return result


def _get_data():
    response = rq.get(future)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find_all('div', class_='push')
    result = []
    for div in body:
        # time, name, content
        data = [div.find('span', class_='push-ipdatetime').text.strip(),
                div.find('span', class_='f3 hl push-userid').text.strip(),
                div.find('span', class_='f3 push-content').text.strip().replace(': ', '')]
        result.append(data)

    return result
