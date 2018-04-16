from selenium import webdriver


# chromedrive 위치
driver = webdriver.Chrome('/home/thenry/Documents/projects/scrapping/chromedriver')

# 3초 기다림
driver.implicitly_wait(3)
# 주소 가져옴
driver.get('https://www.naver.com/')
# 찾고싶은 내용을 XPath로 검색하고 클릭함
driver.find_element_by_xpath('//*[@id="PM_ID_serviceNavi"]/li[9]/a').click()
driver.find_element_by_xpath('//*[@id="menu"]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="content"]/div[3]/ul/li[1]/div/a').click()
# 만화 목록이 있는 테이블을 찾는다
elements = driver.find_elements_by_xpath('//*[@id="content"]/table/tbody/tr')

for item in elements:
    # 검색된 각각의 tr 내부의 td들을 찾는다
    results = item.find_elements_by_css_selector('td')
    # tr중에서 배너들을 거르기 위해서 td가 1개가 넘는것들만 거른다
    if len(results) > 1:
        for temp in results:
            # 결과를 텍스트 형태로 나타냄
            print(temp.text)


#닫기
print(driver.current_url)
driver.close()
