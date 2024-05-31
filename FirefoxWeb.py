from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # 替换为你的Firefox路径
service = Service('D:/job/reptile/firefox/geckodriver.exe')  # 如果你的geckodriver不在PATH中，也需要指定路径
browser = webdriver.Firefox(service=service, options=options)

# 打开网页
browser.get('http://prod.pinyiche.club/index')

time.sleep(5)

# 等待某个元素加载（可选，如果页面加载后需要等待某些JavaScript渲染的内容）
# try:
#     element = WebDriverWait(browser, 20).until(
#         EC.presence_of_element_located((By.ID, "some_element_id"))
#     )
# except:
#     print("Element not found after 10 seconds.")

# 等待用户名和密码输入框出现（可选，但推荐）
# username_input = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'el-input__inner'))  # 替换为实际的ID或其他定位器
# )
# password_input = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, 'el-id-268-26'))  # 替换为实际的ID或其他定位器
# )
username_inputs = browser.find_elements(By.CLASS_NAME, 'el-input__inner')
for username_input in username_inputs:
    if username_input.accessible_name == '请输入用户名':
        username_input.send_keys('1')
    if username_input.accessible_name == '请输入密码':
        username_input.send_keys('1')# 替换为你的用户名

buttons = browser.find_elements(By.CLASS_NAME, 'el-button')
for button in buttons:
    if button.accessible_name == '登录':
        button.click()
time.sleep(5)

menus = browser.find_elements(By.CLASS_NAME, 'v-menu__title')
for menu in menus:
    if menu.text == '团无界运维':
        menu.click()
        break

menus = browser.find_elements(By.CLASS_NAME, 'v-menu__title')
for menu in menus:
    if menu.text == '订单管理':
        menu.click()
        break

menus = browser.find_elements(By.CLASS_NAME, 'v-menu__title')
for menu in menus:
    if menu.text == '快递商品订单管理':
        menu.click()
        break


# 获取页面源代码
source_code = browser.page_source
print(source_code)

time.sleep(5)
# 你还可以对页面上的元素进行操作，例如点击按钮、填写表单等
# ...

# 关闭浏览器
browser.quit()
