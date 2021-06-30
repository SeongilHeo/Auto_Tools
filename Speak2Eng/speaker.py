from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# webdriver 실행
driver = webdriver.Chrome('C:/Users/user/chromedriver.exe')
url='https://dict.naver.com'
driver.get(url)

# 입력 + 검색
input_box=driver.find_element_by_id("ac_input")
input_box.send_keys(Keys.CONTROL, 'v')
input_box.send_keys(Keys.ENTER)

# play
speaker=driver.find_element_by_class_name('play')
speaker.click()

# end
time.sleep(3)
driver.quit()