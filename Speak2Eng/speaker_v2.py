from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
import time

# headless 옵션 추가
options=webdriver.ChromeOptions()
options.add_argument('headless')

# webdriver 실행
driver = webdriver.Chrome('chromedriver.exe',options=options)
txt=pyperclip.paste()
url="https://en.dict.naver.com/#/search?range=all&query="+txt
driver.get(url)
driver.implicitly_wait(3)

# play
speaker=driver.find_element_by_class_name('play')
speaker.click()

# end
time.sleep(3)
driver.quit()