import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_data(url):
    # 发送 HTTP GET 请求
    response = requests.get(url)
    response.encoding = 'utf-8'

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')


        # 注意：这里我们假设第一段内容是紧随标题之后的第一个 <p> 标签
        title = soup.find("title").text

        # 打印结果
        print(f"Title: {title}")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    # 使用函数抓取 Wikipedia 的 "Python" 页面
fetch_wikipedia_data("http://prod.pinyiche.club/twjmgr/audit/member-leader-apply")