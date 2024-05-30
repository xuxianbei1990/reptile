from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 创建ChromeOptions对象
chrome_options = webdriver.ChromeOptions()

# 添加忽略证书错误的参数
chrome_options.add_argument('--ignore-certificate-errors')

driver_path = ChromeDriverManager().install()  # 安装并返回安装成功的路径
browser = webdriver.Chrome(service=Service(driver_path), options=chrome_options)  # 使用对应路径下的driver驱动Chrome

# 打开一个网页
url = 'http://prod.pinyiche.club/twjmgr/audit/member-leader-apply'  # 替换为你想要打开的网页URL
browser.get(url)

# 在这里，你可以添加更多的代码来与页面进行交互，如点击按钮、填写表单等。
# 例如，等待某个元素加载完成：
try:
    element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "myElement"))
    )
    print("Element found and loaded")
except:
    print("Element not found or timed out")

# 当你完成与页面的交互后，关闭浏览器
browser.quit()
