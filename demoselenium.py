import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4

iedriver = "C:\myfile\IEDriverServer_x64_3.4.0\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver  #调用IE浏览器
url = 'http://www.snsingwq.com/index.jsp'
browser = webdriver.Ie(iedriver)
c = browser.get(url)  #需要打开的网址
print(c)


user = browser.find_element_by_id("sulname") #审查元素username的id
user.send_keys("edit@snsing.com")  #输入账号
password = browser.find_element_by_name("sulpass") #审查元素password的name
password.send_keys("zhonghuawenhua")  #输入密码
randomcode = browser.find_element_by_name("rand").text
print(randomcode)
code = browser.find_element_by_name("rand").send_keys(randomcode)

password.send_keys(Keys.RETURN) #实现自动点击登陆
print('登陆成功')
