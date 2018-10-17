from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.zhihu.com')
print(driver.page_source)

