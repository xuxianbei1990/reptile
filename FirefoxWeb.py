from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # 替换为你的Firefox路径
service = Service('D:/job/reptile/firefox/geckodriver.exe')  # 如果你的geckodriver不在PATH中，也需要指定路径
browser = webdriver.Firefox(service=service, options=options)


# 打开网页
browser.get('http://prod.pinyiche.club/index')

# 等待某个元素加载（可选，如果页面加载后需要等待某些JavaScript渲染的内容）
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "some_element_id"))
    )
except:
    print("Element not found after 10 seconds.")

# 获取页面源代码
source_code = browser.page_source
print(source_code)

# 你还可以对页面上的元素进行操作，例如点击按钮、填写表单等
# ...

# 关闭浏览器
browser.quit()