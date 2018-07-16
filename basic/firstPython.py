import urllib.request

# page = urllib.request.urlopen('http://www.baidu.com')
# html = page.read()
# print(html)
#
# pageFile = open('pageCode.txt', 'wb+')
# pageFile.write(html)
# pageFile.close()

def get_html(url):
    page = urllib.request.urlopen('http://www.baidu.com')
    html = page.read()
    return html

