from selenium import webdriver


driver = webdriver.Chrome('/home/thenry/Documents/projects/scrapping/chromedriver')
driver.implicitly_wait(3)
driver.get('https://first.wifi.olleh.com/starbucks/index_kr.html')
driver.find_element_by_xpath('//*[@id="agreement_agree"]').click()
driver.close()
