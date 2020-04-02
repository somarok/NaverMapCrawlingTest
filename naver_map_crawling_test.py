
# -*- coding: euc-kr -*- 

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException

def get_info():
    delay = 15  # 
    try:
            WebDriverWait(driver, delay).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, '#container > div.router-output > shrinkable-layout > search-layout > search-entry > entry-layout > entry-place > div > div.scroll_area > div > div.scroll_box > div.summary_area.type_search.ng-star-inserted > div.summary_title_box > strong')
                )
            )
            el_title=driver.find_element_by_css_selector('#container > div.router-output > shrinkable-layout > search-layout > search-entry > entry-layout > entry-place > div > div.scroll_area > div > div.scroll_box > div.summary_area.type_search.ng-star-inserted > div.summary_title_box > strong')
            el_img=driver.find_element_by_class_name('img_photo')
            img_url=el_img.get_attribute('src')

            strTitle=el_title.text
            print('shopName: ', strTitle)
            print('imgLink: ',img_url)
            
    except ElementNotVisibleException:
            print('no tags')
           
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://map.naver.com/v5/search/%ED%99%8D%EB%8C%80%EB%98%90%EB%B3%B4%EA%B2%A0%EC%A7%80%EB%96%A1%EB%B3%B6%EC%9D%B4/place/37663862")

ele_closebtn = driver.find_element_by_xpath('//*[@id="intro_popup_close"]')
if ele_closebtn:
   ele_closebtn.click()

get_info()

driver.close()