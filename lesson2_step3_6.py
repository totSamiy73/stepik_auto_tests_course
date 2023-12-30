#вдруг не оценили Meaningful message
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.window_handles[1])
    print(browser.window_handles[0])
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(1)
    browser.quit()