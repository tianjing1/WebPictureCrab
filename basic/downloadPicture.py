
import re
import urllib


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imageList = re.findall(imgre, html)
    x = 0
    for imgurl in imageList:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
    return imageList


html = get_html("http://tieba.baidu.com/p/2460150866")
print(getImg(html))
