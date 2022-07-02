import urllib.request
import xpinyin
from bs4 import BeautifulSoup

def get_weather(city_pinyin):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    website = "http://www.tianqi.com/" + city_pinyin + ".html"
    req = urllib.request.Request(url=website,headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")  #html.parser表示解析使用的解析器
    nodes = soup.find_all('dd')
    tody_weather = ""
    for node in nodes:
        temp = node.get_text()
        if (temp.find('[切换城市]')):
            temp = temp[:temp.find('[切换城市]')]
        tody_weather += temp
    return tody_weather

if __name__ == "__main__":
    pin = xpinyin.Pinyin()
    city_pinyin = pin.get_pinyin("杭州","")
    tody_weather = get_weather(city_pinyin)
    print(tody_weather)